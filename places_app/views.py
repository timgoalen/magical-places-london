from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.conf import settings
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    get_list_or_404,
)
from .models import Place, Comment, Favourite
from .forms import AddPlaceForm, CommentForm
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


def home_page_view(request):
    """
    VIEW: display the map page.
    """
    # Annotate the Place objects with their related field comments count.
    places_including_comments_count = Place.objects.annotate(
        comments_count=Count("comments")
    )

    # Send the data from the databse to the template,
    # to be picked up by JavaScript.
    context = {
        # Return a list of dictionaries for each row in the database.
        "places_list_of_dicts": list(
            places_including_comments_count.values(
                "id",
                "place_name",
                "latitude",
                "longitude",
                "address",
                "google_place_id",
                "comments_count",
            )
        ),
        "api_key": settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, "home.html", context)


def place_list_view(request):
    """
    VIEW: display the list view page.
    """
    places = Place.objects.all()
    user = request.user
    favourites = Favourite.objects.all()

    # Establish user 'favourites' list.
    if user.is_authenticated:
        user_favourites = Place.objects.filter(favourites__user=user)
    else:
        user_favourites = []

    # Get 'sort' options from user.
    sort_by = request.GET.get("sort", "default")

    if sort_by == "a-z":
        places = Place.objects.order_by("place_name")
    elif sort_by == "newest":
        places = Place.objects.order_by("-created_on")
    elif sort_by == "user_favourites":
        user_favourites = user_favourites.order_by("-created_on")

    # Render the template with the sorted places,
    # and the selected 'sort_by' value.
    context = {
        "places": places,
        "sort_selection": sort_by,
        "user_favourites": user_favourites,
        "favourites": favourites,
        "api_key": settings.GOOGLE_MAPS_API_KEY,
        # Send a list of dictionaris with the Google Place IDs,
        # for getting photos from Google.
        "places_list_of_dicts": list(
            places.values(
                "id",
                "google_place_id",
            )
        ),
    }

    return render(request, "list_view.html", context)


def place_detail_view(request, pk):
    """
    VIEW: display the Place detail page.
    """
    place = get_object_or_404(Place, pk=pk)
    user = request.user

    # Establish a user 'favourites' list.
    if user.is_authenticated:
        user_favourites = Place.objects.filter(favourites__user=user)
    else:
        user_favourites = []

    # Check whether the user has favourited this place.
    user_has_favourited = False
    if user.is_authenticated:
        user_has_favourited = Favourite.objects.filter(
                                place=place, user=user).exists()

    # Comment Form functionality:
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = user
            comment.place = place
            comment.created_on = timezone.now()
            comment.save()
            messages.success(request, "Thanks for your comment!")
            return redirect("place_detail", pk)
    else:
        form = CommentForm()

    # Context:
    context = {
        "place": place,
        "form": CommentForm(),
        "user_favourites": user_favourites,
        "user_has_favourited": user_has_favourited,
        "api_key": settings.GOOGLE_MAPS_API_KEY,
    }

    return render(request, "place_detail.html", context)


class PlaceCreateView(LoginRequiredMixin, CreateView):
    """
    VIEW: display the 'Add Place' page.
    """
    model = Place
    template_name = "place_add.html"
    form_class = AddPlaceForm

    def form_valid(self, form):
        """
        Override 'form_valid' to assign logged-in user to 'contributer'.
        """
        form.instance.contributer = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "Thanks for creating a new Place!")

        return response

    def form_invalid(self, form):
        """
        Override 'form_invalid' to handle duplicate place submissions.
        """
        if "place_name" in form.errors:
            messages.error(
                self.request, "A place with this name already exists."
                )
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        """
        Override 'get_context_data'.
        """
        context = super().get_context_data(**kwargs)
        # Add additional context data for Google Places autocomplete.
        context["api_key"] = settings.GOOGLE_MAPS_API_KEY

        return context


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    VIEW: display the 'Edit Comment' page.
    """
    model = Comment
    template_name = "comment_edit.html"
    fields = [
        "comment",
    ]
    # Set fallback success URL.
    success_url = reverse_lazy("place_detail")

    def form_valid(self, form):
        """
        Assign current time & date to 'updated_on'.
        """
        form.instance.updated_on = timezone.now()
        response = super().form_valid(form)
        messages.success(self.request, "Your comment was succesfully updated")

        return response

    def get_success_url(self):
        """
        Take user back to the 'place_detail' page associated with the comment.
        """
        place = self.object.place
        return reverse_lazy("place_detail", args=[place.pk])

    def test_func(self):
        """
        Test that logged in user is the comment author.
        """
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    VIEW: Display the 'Delete Comment' page.
    """
    model = Comment
    template_name = "comment_delete.html"
    # Set fallback success URL.
    success_url = reverse_lazy("list")

    def get_success_url(self):
        """
        Redirect back to the 'place_detail' page associated with the comment.
        """
        place = self.object.place
        messages.success(self.request, "Your comment was succesfully deleted")

        return reverse_lazy("place_detail", args=[place.pk])

    def test_func(self):
        """
        Test that logged in user is comment author.
        """
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False


@login_required
def favourite_places_view(request, pk):
    """
    VIEW: handle the logic for the 'favourite'/'unfavourite' buttons.
    """
    place = get_object_or_404(Place, id=request.POST.get("place_id"))
    user = request.user
    existing_favourite = Favourite.objects.filter(
                        place=place, user=user).first()

    if existing_favourite:
        existing_favourite.delete()
    else:
        new_favourite = Favourite(place=place, user=user)
        new_favourite.save()

    referring_url = request.META.get("HTTP_REFERER", None)
    sectionId = "#" + str(pk)

    # Redirect user to the page that they used the 'favourite' button on,
    # e.g. 'List View' or 'Detail View'.
    if referring_url:
        if "list_view" in referring_url:
            return HttpResponseRedirect(referring_url + sectionId)
        else:
            return HttpResponseRedirect(referring_url)
    else:
        return HttpResponseRedirect(reverse("home"))


def handle404(request, exception):
    """
    404 error page.
    """
    return render(request, '404.html', status=404)


def handle500(request):
    """
    500 error page.
    """
    return render(request, '500.html', status=500)

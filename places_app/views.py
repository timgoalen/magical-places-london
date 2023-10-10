# **remove unused ones...
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.conf import settings
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    get_list_or_404,
)  # need reverse?
from .models import Place, Comment, Favourite
from .forms import AddPlaceForm, CommentForm
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.db.models import Count
from django.contrib import messages


# Main page view


def home_page_view(request):
    # Annotate the Place objects with their related field comments count
    places_including_comments_count = Place.objects.annotate(
        comments_count=Count("comments")
    )

    context = {
        # Return a list of dictionaries for each row in the database,
        "places_list_of_dicts": list(
            places_including_comments_count.values(
                "id",
                "place_name",
                "latitude",
                "longitude",
                "address",
                "photo_url",
                "comments_count",
            )
        ),
        "api_key": settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, "home.html", context)


# List page view


def place_list_view(request):
    places = Place.objects.all()
    user = request.user
    favourites = Favourite.objects.all()

    # Establish user 'favourites' list
    if user.is_authenticated:
        user_favourites = Place.objects.filter(favourites__user=user)
    else:
        user_favourites = []

    # Get 'sort' options from user
    sort_by = request.GET.get("sort", "default")

    if sort_by == "a-z":
        places = Place.objects.order_by("place_name")
    elif sort_by == "newest":
        places = Place.objects.order_by("-created_on")
    elif sort_by == "user_favourites":
        user_favourites = user_favourites.order_by("-created_on")
        # places = user_favourites

    # Render the template with the sorted places and the selected sort_by value
    context = {
        "places": places,
        "sort_selection": sort_by,
        "user_favourites": user_favourites,
        "favourites": favourites,  # need this one?(does it send favourites form all users?)
    }

    return render(request, "list_view.html", context)


# Place Detail views


def place_detail_view(request, pk):
    place = get_object_or_404(Place, pk=pk)
    user = request.user

    # Establish user 'favourites' list
    if user.is_authenticated:
        user_favourites = Place.objects.filter(favourites__user=user)
    else:
        user_favourites = []

    # Check whether the user has favourited this place
    user_has_favourited = False
    if user.is_authenticated:
        user_has_favourited = Favourite.objects.filter(place=place, user=user).exists()

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
        # refactor into 1 ???...
        "user_favourites": user_favourites,
        "user_has_favourited": user_has_favourited,
    }

    return render(request, "place_detail.html", context)


# Place CRUD views


class PlaceCreateView(CreateView):
    model = Place
    template_name = "place_add.html"
    form_class = AddPlaceForm

    # Override form_valid to assign logged-in user to 'contributer'
    def form_valid(self, form):
        form.instance.contributer = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "Thanks for creating a new Place!")

        return response

    # Override form_invalid to handle duplicate place submissions
    def form_invalid(self, form):
        if "place_name" in form.errors:
            messages.error(self.request, "A place with this name already exists.")
        return super().form_invalid(form)

    # Override get_context_data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context data for Google Places autocomplete
        context["api_key"] = settings.GOOGLE_MAPS_API_KEY

        return context


# ** NOT USED AT THE MOMENT
class PlaceUpdateView(UpdateView):
    model = Place
    template_name = "place_edit.html"
    fields = ["place_name", "latitude", "longitude"]

    # Assign current time & date to 'updated_on'
    def form_valid(self, form):
        form.instance.updated_on = timezone.now()  # change to 'add_now'etc?
        return super().form_valid(form)


# Comment CRUD views


class CommentUpdateView(UpdateView):
    model = Comment
    template_name = "comment_edit.html"
    fields = [
        "comment",
    ]
    # Fallback success URL:
    success_url = reverse_lazy("place_detail")

    # # Assign current time & date to 'updated_on'
    # STILL NEED THIS???
    def form_valid(self, form):
        form.instance.updated_on = timezone.now()
        response = super().form_valid(form)
        messages.success(self.request, "Your comment was succesfully updated")

        return response

    # Success URL takes user back to the 'place_detail page associated with the comment
    def get_success_url(self):
        place = self.object.place
        return reverse_lazy("place_detail", args=[place.pk])


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = "comment_delete.html"
    # Fallback success URL:
    success_url = reverse_lazy("list")

    # Success URL takes user back to the 'place_detail page associated with the comment
    def get_success_url(self):
        place = self.object.place
        messages.success(self.request, "Your comment was succesfully deleted")

        return reverse_lazy("place_detail", args=[place.pk])


# Favourites


def favourite_places_view(request, pk):
    place = get_object_or_404(Place, id=request.POST.get("place_id"))
    user = request.user
    existing_favourite = Favourite.objects.filter(place=place, user=user).first()

    if existing_favourite:
        existing_favourite.delete()
    else:
        new_favourite = Favourite(place=place, user=user)
        new_favourite.save()

    referring_url = request.META.get("HTTP_REFERER", None)
    sectionId = "#" + str(pk)

    # ** explain logic...so you can favourite places in the list view and it takes you back rthere istead of detail view
    if referring_url:
        if "list_view" in referring_url:
            return HttpResponseRedirect(referring_url + sectionId)
        else:
            return HttpResponseRedirect(referring_url)
    else:
        return HttpResponseRedirect(reverse("home"))

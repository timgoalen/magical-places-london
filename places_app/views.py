from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Place, Comment
from django.conf import settings
from .forms import CommentForm


# Main pages views


def home_page_view(request):
    # Return a list of dictionaries for each row in the database
    # (specifying the 3 values hides the Primary Key number) [not done at the moment]
    context = {
        "places": list(Place.objects.values()),
        "api_key": settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, "home.html", context)


class ListPageView(ListView):
    model = Place
    template_name = "list_view.html"
    queryset = Place.objects.order_by("-created_on")
    # USE IF NEEDED: (check 'Creating Our First View' video to
    # see what code you need in template for pagination)
    # paginate_by = 6


# Place views


class PlaceDetailView(View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


# class PlaceDetailView(View):
#     def get(self, request, *args, **kwargs):
#         queryset = Place.objects.filter(pk=self.request.Place.pk)
#         place = get_object_or_404(queryset, pk=pk)
#         comments = place.comments.order_by("-created_on")
#         favourited = False
#         if place.favourited.filter(id=self.request.user.id).exists():
#             liked = True

#             return render(
#                 request,
#                 "place_detail.html",
#                 {
#                     "place": place,
#                     "comments": comments,
#                     "commented": False,
#                     "favourited": favourited,
#                     "comment_form": CommentForm(),
#                 },
#             )


class PlaceCreateView(CreateView):
    model = Place
    template_name = "place_add.html"
    fields = ["place_name", "latitude", "longitude"]


class PlaceUpdateView(UpdateView):
    model = Place
    template_name = "place_edit.html"
    fields = ["place_name", "latitude", "longitude"]


# Comment views


class CommentGet(DetailView):
    model = Place
    template_name = "place_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Place
    form_class = CommentForm
    template_name = "place_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.place = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        place = self.get_object()
        return reverse("place_detail", kwargs={"pk": place.pk})

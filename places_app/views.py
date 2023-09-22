# **remove unused ones...
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Place, Comment
from django.conf import settings
from .forms import CommentForm
from django.utils import timezone


# Main page view


def home_page_view(request):
    context = {
        # Return a list of dictionaries for each row in the database,
        # (specifying the 3 values hides the Primary Key number) [not done at the moment]
        "places_list_of_dicts": list(
            Place.objects.values("id", "place_name", "latitude", "longitude")
        ),
        "api_key": settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, "home.html", context)


# List page view


def place_list_view(request):
    context = {"places": Place.objects.all().order_by("-created_on")}

    return render(request, "list_view.html", context)


# Place Detail views


def place_detail_view(request, pk):
    place = get_object_or_404(Place, pk=pk)
    # Comment Form functionality:
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.place = place
            comment.created_on = timezone.now()
            comment.save()
            return redirect("place_detail", pk)
    else:
        form = CommentForm()
    # Context:
    context = {"place": place, "form": CommentForm()}

    return render(request, "place_detail.html", context)


# Place CRUD views


class PlaceCreateView(CreateView):
    model = Place
    template_name = "place_add.html"
    fields = [
        "place_name",
        "latitude",
        "longitude",
    ]

    # Assign logged-in user to 'contributer'
    def form_valid(self, form):
        form.instance.contributer = self.request.user
        return super().form_valid(form)


class PlaceUpdateView(UpdateView):
    model = Place
    template_name = "place_edit.html"
    fields = ["place_name", "latitude", "longitude"]

    # Assign current time & date to 'updated_on'
    def form_valid(self, form):
        form.instance.updated_on = timezone.now()
        return super().form_valid(form)


# Comment CRUD views


class CommentUpdateView(UpdateView):
    model = Comment
    template_name = "comment_edit.html"
    fields = ["comment",]

    # Assign current time & date to 'updated_on'
    def form_valid(self, form):
        form.instance.updated_on = timezone.now()
        return super().form_valid(form)

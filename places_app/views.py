# remove TemplateView if not using
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.conf import settings
from django.shortcuts import render
from .models import Place, Comment
from django.conf import settings


def home_page_view(request):
    # places = Place.objects.all()
    # comments = Place.comment_set
    # Return a list of dictionaries for each row in the database
    # (specifying the 3 values hides the Primary Key number)
    context = {
        # "places": places,
        # "comments": comments,
        # "places": list(Place.objects.values("place_name", "latitude", "longitude")),
        "places": list(Place.objects.values()),
        # "comments": list(Comment.objects.values("place_name", "comment")),
        "api_key": settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, "home.html", context)


class ListPageView(ListView):
    model = Place
    template_name = "list_view.html"


class PlaceDetailView(DetailView):
    model = Place
    template_name = "place_detail.html"


class PlaceCreateView(CreateView):
    model = Place
    template_name = "place_add.html"
    fields = ["place_name", "latitude", "longitude"]


class PlaceUpdateView(UpdateView):
    model = Place
    template_name = "place_edit.html"
    fields = ["place_name", "latitude", "longitude"]

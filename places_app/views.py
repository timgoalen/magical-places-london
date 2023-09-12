# remove TemplateView if not using
from django.views.generic import TemplateView, ListView, DetailView
from django.conf import settings
from django.shortcuts import render
from .models import Place, Comment
from django.conf import settings


def home_page_view(request):
    # Return a list of dictionaries for each row in the database
    # (specifying the 3 values hides the Primary Key number)
    context = {
        "places": list(Place.objects.values("place_name", "latitude", "longitude")),
        "comments": list(Comment.objects.values("place_name", "comment")),
        "api_key": settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, "home.html", context)


class ListPageView(ListView):
    model = Place
    template_name = "list_view.html"


class PlaceDetailView(DetailView):
    model = Place
    template_name = "place_detail.html"

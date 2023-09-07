# remove TemplateView if not using
from django.views.generic import TemplateView, ListView, DetailView

# remove this if not using:(if only using generic views)
from django.shortcuts import render
from .models import Place
from django.conf import settings


# class HomePageView(TemplateView):
#     model = Place
#     template_name = "home.html"


def home_page_view(request):
    # Return a list of dictionaries for each row in the database
    # (specifying the 3 values hides the Primary Key number)
    context = {
        "places": list(Place.objects.values("place_name", "latitude", "longitude"))
    }
    return render(request, "home.html", context)


class ListPageView(ListView):
    model = Place
    template_name = "list_view.html"


class PlaceDetailView(DetailView):
    model = Place
    template_name = "place_detail.html"

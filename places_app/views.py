# **remove unused ones...
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.conf import settings
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Place, Comment
from django.conf import settings
from .forms import CommentForm


# Main pages views


def home_page_view(request):
    context = {
        # Return a list of dictionaries for each row in the database,
        # (specifying the 3 values hides the Primary Key number) [not done at the moment]
        "places_list_of_dicts": list(Place.objects.values()),
        "api_key": settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, "home.html", context)


# List page view


def place_list_view(request):
    context = {"places": Place.objects.all().order_by("-created_on")}

    return render(request, "list_view.html", context)


# Place Detail views


class PlaceDetailView(DetailView):
    model = Place
    template_name = "place_detail.html"


def place_detail_view(request, pk):
    context = {"place": get_object_or_404(Place, pk=pk)}

    return render(request, "place_detail.html", context)


# class ListPageView(ListView):
#     model = Place
#     template_name = "list_view.html"
#     queryset = Place.objects.order_by("-created_on")


# Place CRUD views


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

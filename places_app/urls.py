from django.urls import path
from .views import (
    home_page_view,
    ListPageView,
    PlaceDetailView,
    PlaceCreateView,
    PlaceUpdateView,
)


urlpatterns = [
    path("place/add/", PlaceCreateView.as_view(), name="place_add"),
    path("place/<int:pk>/", PlaceDetailView.as_view(), name="place_detail"),
    path("place/<int:pk>/edit/", PlaceUpdateView.as_view(), name="place_edit"),
    path("list_view/", ListPageView.as_view(), name="list"),
    path("", home_page_view, name="home"),
]

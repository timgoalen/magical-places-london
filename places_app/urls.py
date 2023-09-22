from django.urls import path
from .views import (
    home_page_view,
    place_list_view,
    place_detail_view,
    PlaceCreateView,
    PlaceUpdateView,
)


urlpatterns = [
    path("place/add/", PlaceCreateView.as_view(), name="place_add"),
    # path("place/<int:pk>/", PlaceDetailView.as_view(), name="place_detail"),
    path("place/<int:pk>/", place_detail_view, name="place_detail"),
    path("place/<int:pk>/edit/", PlaceUpdateView.as_view(), name="place_edit"),
    path("list_view/", place_list_view, name="list"),
    path("", home_page_view, name="home"),
]

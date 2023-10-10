from django.urls import path
from .views import (
    home_page_view,
    place_list_view,
    place_detail_view,
    PlaceCreateView,
    CommentUpdateView,
    CommentDeleteView,
    favourite_places_view,
)


urlpatterns = [
    path("", home_page_view, name="home"),
    path("place/add/", PlaceCreateView.as_view(), name="place_add"),
    path("place/<int:pk>/", place_detail_view, name="place_detail"),
    path("comment/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment_edit"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
    path("favourites/<int:pk>", favourite_places_view, name="favourite_a_place"),
    path("list_view/", place_list_view, name="list"),
]

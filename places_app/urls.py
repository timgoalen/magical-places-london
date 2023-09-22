from django.urls import path
from .views import (
    home_page_view,
    place_list_view,
    place_detail_view,
    PlaceCreateView,
    PlaceUpdateView,
    CommentUpdateView,
)


urlpatterns = [
    path("place/add/", PlaceCreateView.as_view(), name="place_add"),
    path("place/<int:pk>/", place_detail_view, name="place_detail"),
    path("place/<int:pk>/edit/", PlaceUpdateView.as_view(), name="place_edit"),
    path("comment/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment_edit"),
    path("list_view/", place_list_view, name="list"),
    path("", home_page_view, name="home"),
]

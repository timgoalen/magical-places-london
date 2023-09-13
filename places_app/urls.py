from django.urls import path
from .views import home_page_view, ListPageView, PlaceDetailView, PlaceCreateView


urlpatterns = [
    path("place/add/", PlaceCreateView.as_view(), name="place_add"),
    path("place/<int:pk>/", PlaceDetailView.as_view(), name="place_detail"),
    path("list_view/", ListPageView.as_view(), name="list"),
    path("", home_page_view, name="home"),
]

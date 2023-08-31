from django.urls import path
from .views import HomePageView, ListPageView


urlpatterns = [
    path("list_view/", ListPageView.as_view(), name="list"),
    path("", HomePageView.as_view(), name="home"),
]

from django.urls import path
from .views import home_page_view, ListPageView


urlpatterns = [
    path("list_view/", ListPageView.as_view(), name="list"),
    path("", home_page_view, name="home"),
]

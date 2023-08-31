from django.views.generic import TemplateView, ListView
from .models import Place


class HomePageView(TemplateView):
    template_name = "home.html"


class ListPageView(ListView):
    model = Place
    template_name = "list_view.html"

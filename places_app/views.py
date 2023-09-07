from django.views.generic import TemplateView, ListView
from .models import Place
from django.conf import settings


class HomePageView(TemplateView):
    template_name = "home.html"


class ListPageView(ListView):
    model = Place
    template_name = "list_view.html"


# def HomePageView(request):
#     template_name = "home.html"
#     context = {
#         'api_key': settings.GOOGLE_MAPS_API_KEY
#     }
#     return render('home.html', context)

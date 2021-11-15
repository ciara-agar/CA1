from django.http import HttpResponse

from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Post


def homePageView(request):
    return HttpResponse('')


class HomePageView(TemplateView):
    template_name = 'home.html'

class HomePageView(ListView):
    model = Post 
    template_name = 'home.html'
    context_object_name = "all_posts_lists" 



from django.views.generic import ListView

from .models import Request

class RequestListView(ListView):
    model = Request
    template_name = 'request.html'
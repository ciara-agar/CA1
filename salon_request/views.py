from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Request

class RequestListView(ListView):
    model = Request
    template_name = 'request_.html'
    context_object_name = 'all_requests_list'

class RequestDetailView(DetailView):
    model = Request
    template_name = 'request_detail.html'

class RequestCreateView(CreateView):
    model = Request
    template_name = 'request_new.html'
    fields = ['title', 'author', 'body']

class RequestUpdateView(UpdateView):
    model = Request
    template_name = 'request_edit.html'
    fields = ['title', 'body']

class RequestDeleteView(DeleteView):
    model = Request
    template_name = 'request_delete.html'
    success_url = reverse_lazy('home')

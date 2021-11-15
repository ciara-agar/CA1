from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from django.urls import reverse_lazy
from .models import Reviews

class RequestListView(ListView):
    model = Reviews
    template_name = 'reviewpost_list.html'
    context_object_name = 'all_requests_list'

class ReviewsListView(ListView):
    model = Reviews
    template_name = 'home/html'
    context_object_name = 'all_posts_list'
    
class ReveiwsDetailView(DetailView):
    model = Reviews
    template_name = 'reviewpost_detail.html'


class ReviewsCreateView(CreateView):
    model = Reviews 
    template_name = 'reviewpost_new.html'
    fields = ['title', 'author', 'body']


class ReviewsUpdateView(UpdateView):
    model = Reviews 
    template_name = 'reviewpost_edit.html'
    fields = ['title', 'body']

class ReviewsDeletelView(DeleteView):
    mmodel = Reviews 
    template_name = 'reviewpost_delete.html'
    success_url = reverse_lazy('home')
from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'detail_view.html'

class ViewCreate(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'
    
class UpdateViewPost(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body']
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
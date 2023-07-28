from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Post


# Create your views here.

class Homepage(ListView):
    model = Post 
    template_name = 'home.html'
    context_object_name = 'message_posts'
class Aboutpage(ListView):
    model = Post
    template_name = 'about.html'
    context_object_name = 'message_posts'

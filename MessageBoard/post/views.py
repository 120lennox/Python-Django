from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Post


# Create your views here.

class Homepage(TemplateView):
    template_name = 'home.html'

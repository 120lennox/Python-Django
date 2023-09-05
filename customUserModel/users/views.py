from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import CreateView

# Create your views here.

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

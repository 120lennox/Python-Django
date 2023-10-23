from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserRegistration

# Create your views here.
class SignupView(CreateView):
    form_class = CustomUserRegistration
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
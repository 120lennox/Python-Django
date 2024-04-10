from typing import Any
from django.shortcuts import render
from .models import Airport, Flights
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'flights/index.html'
    model = Flights

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["flights"] = Flights.objects.all()
        return context #fixed bug. 
    
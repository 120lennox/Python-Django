from typing import Any
from django.shortcuts import render
from .models import Airport, Flights
from django.views.generic import TemplateView, DetailView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'flights/index.html'
    model = Flights

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["flights"] = Flights.objects.all()
        return context #fixed bug. Template View if given a get context behavior returns the context

class FlightView(DetailView):
    template_name = 'flights/flight.html'

    def get_context_data(flight_id):
        context = super().get_context_data()
        context["flight"] = Flights.objects.get(pk=flight_id)
        return context
        
    
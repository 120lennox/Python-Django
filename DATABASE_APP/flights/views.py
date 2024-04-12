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
    model = Flights
    template_name = 'flights/flight.html'
    context_object_name = "flight" 
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        flight = self.get_object()
        context['flight_id'] = flight.pk

        return context
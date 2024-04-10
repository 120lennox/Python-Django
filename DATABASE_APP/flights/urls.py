from django.urls import path
from .views import HomePageView, FlightView

urlpatterns = [
    path("", HomePageView.as_view(), name="index"), 
    path("<int:pk>", FlightView.as_view(), name="flight")
]

from .views import *
from django.urls import path

urlpatterns = [
    path('', Homepage.as_view(), name='home')
]

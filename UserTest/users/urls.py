from django.urls import path
from .views import *

urlpatterns = [
    path('', Home_view.as_view(), name='index'),
]

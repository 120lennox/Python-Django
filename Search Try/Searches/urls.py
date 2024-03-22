from django.urls import path
from .views import *

urlpatterns = [
    path("", HomepageView.as_view(), name='home'),
    path("add", AddResults.as_view(), name="add")
]

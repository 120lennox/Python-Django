from django.urls import path
from . views import *

app_name = "tasks"
urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("add", AddTask.as_view(), name="add"),
]

from django.urls import path
from .views import HomepageView, AddResults, SearchView

urlpatterns = [
    path("", HomepageView.as_view(), name='home'),
    path("add", AddResults.as_view(), name="add"),
    path("search", SearchView.as_view(), name='search')
]

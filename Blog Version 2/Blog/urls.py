from django.urls import path
from .views import *

urlpatterns = [
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='post_delete'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='detail_view'),
    path('post/<int:pk>/edit', UpdateViewPost.as_view(), name='post_edit'),
    path('', HomePageView.as_view(), name='home'),
    path('new_post', ViewCreate.as_view(), name='post_new')
]
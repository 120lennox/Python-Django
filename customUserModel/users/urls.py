from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_forms.html'), name='password_change'),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(template_name='registration/user_password_changed_done.html'), name='password_changed_done'),
    # the login url
    path('login_now/', LoginView.as_view(template_name = 'registration/login.html'), name='login_now'), 
    #password reset url 
    path('password_reset/', PasswordResetView.as_view(template_name = 'registration/password_reset.html'), name='password_reset'), 
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name = 'registration/password_reset-Done.html'), name='password_reset_done'), 
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name = 'registration/password_reset-confirm.html'), name='password_reset_confirm'), 
    path('password_reset-complete/done/', PasswordResetCompleteView.as_view(template_name = 'registration/password_reset-complete.html'),name='password-reset-completed'),
]

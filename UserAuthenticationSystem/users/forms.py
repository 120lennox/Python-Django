from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = CustomUser
        fields = ('username', 'date_of_birth', 'email')
        
class CustomUserChangeForm(UserChangeForm):
    class Meta():
        model = CustomUser
        fields = ('username', 'date_of_birth', 'email')
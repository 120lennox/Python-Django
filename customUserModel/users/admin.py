from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserchangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff']

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
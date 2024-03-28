from django.contrib import admin
from .models import UserCustomization
from .forms import CustomUserRegistration
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserRegistration
    model = UserCustomization
    list_display = ['first_name', 'last_name', 'email', 'date_of_birth', 'is_staff']
    ordering = ['email']

# Register your models here.    
admin.site.register(UserCustomization, CustomUserAdmin)
from django import forms 
from .models import UserCustomization
from django.utils.translation import gettext_lazy as _

class CustomUserRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = UserCustomization
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'password']
        
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError(_('Passwords do not match'))
        
        return confirm_password
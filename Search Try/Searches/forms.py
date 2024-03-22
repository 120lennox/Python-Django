from django import forms
from .models import Students

class StudentForms(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'grade']
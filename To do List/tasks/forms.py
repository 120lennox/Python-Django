from .models import TasksFields
from django import forms

#defining form fields here

class TaskForms(forms.ModelForm):
    class Meta:
        model = TasksFields
        fields = ['text_tasks']
        
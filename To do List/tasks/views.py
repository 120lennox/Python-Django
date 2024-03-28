from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django import forms
from .models import TasksFields
from .forms import TaskForms

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'tasks\index.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tasks'] = TasksFields.objects.all()
        return context
       
class AddTask(TemplateView):
    template_name = 'tasks/add.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForms()
        
        return context
    
    def post(self, request, *args, **kwargs):
        form = TaskForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:index')
        else:
            return render(request, self.template_name, {
                "form":form
            })
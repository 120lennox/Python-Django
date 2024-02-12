from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'tasks\index.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tasks'] = ['test1', 'test2']
        
        return context
    
class AddTask(TemplateView):
    template_name = 'tasks\add.html'
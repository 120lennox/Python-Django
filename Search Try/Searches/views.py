from typing import Any
from django.shortcuts import render, redirect
from .models import Students
from .forms import StudentForms
from django.views.generic import DetailView, View, TemplateView 

# Create your views here.
class HomepageView(TemplateView):
    model = Students
    template_name = 'Searches/home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['students'] = Students.objects.all()

        return context
    
class AddResults(TemplateView):
    model = Students
    template_name = 'Searches/add_results.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data()
        context['form'] = StudentForms()

        return context
    
    def post(self, request):
        form = StudentForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        else:
            render(request, self.template_name, {
                'form':form
            })
    
import imp
from django.shortcuts import render
from .models import Student
from django.views.generic.base import TemplateView

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'app1/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_objects"] = Student.objects.all().order_by('name') 
        return context
    
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import Student


# Create your views here.
class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'password']
    # Use our own templates
    template_name = 'app1/mytemplate.html'
    ###  We can aslo use the def get_absolute_url(self): in models.py

    # success_url = '/thanks/'


class ThanksTemplateView(TemplateView):
    template_name = 'app1/thanks.html'


class StudentDetailView(DetailView):
    model = Student
from django.forms.widgets import Widget
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import Student
from django import forms
from .forms import StudentModelForm

# Create your views here.
# class StudentCreateView(CreateView):
#     model = Student
#     fields = ['name', 'email', 'password']
#     success_url = '/thanks/'
#     # If we want to add class for using css or anything
#     def get_form(self):
#         form = super().get_form()
#         form.fields['name'].widget = forms.TextInput(attrs={'class' : 'myname'})
#         form.fields['email'].widget = forms.EmailInput(attrs={'class' : 'myemail'})
#         form.fields['password'].widget = forms.PasswordInput(attrs={'class' : 'mypass'})

 # Another way to set class for apply css or bootstrap check the forms.py file
class StudentCreateView(CreateView):
    form_class = StudentModelForm
    # template_name = 'app1/student_form.html'
    template_name = 'app1/student_form.html'
    success_url = '/thanks/'
   


class ThanksTemplateView(TemplateView):
    template_name = 'app1/thanks.html'

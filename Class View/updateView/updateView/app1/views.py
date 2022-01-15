from django.forms import forms
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from .models import Student
from django import forms
from .forms import StudentModelForm

# Create your views here.
# class StudentCreateView(CreateView):
#     model = Student
#     fields = ['name', 'email', 'password']
#     success_url = '/thanks/'


# class ThanksTemplateView(TemplateView):
#     template_name = 'app1/thanks.html'



# class StudentUpdateView(UpdateView):
#     model = Student
#     fields = ['name', 'email', 'password']
#     success_url = '/updatethanks/'

# class StudentUpdateTemplateView(TemplateView):
#     template_name = 'app1/updatethanks.html'

# ============================================================================================================

# Now I will change some code to get the class in form for apply the css

# class StudentCreateView(CreateView):
#     model = Student
#     fields = ['name', 'email', 'password']
#     success_url = '/thanks/'

#     # this function help us to make a class in label for applying css
#     def get_form(self):
#         form = super().get_form()
#         form.fields['name'].widget = forms.TextInput(attrs={'class' : 'myName'})
#         form.fields['email'].widget = forms.EmailInput(attrs={'class' : 'myEmail'})
#         form.fields['password'].widget = forms.PasswordInput(attrs={'class' : 'myPassword'})
#         return form

# class ThanksTemplateView(TemplateView):
#     template_name = 'app1/thanks.html'



# class StudentUpdateView(UpdateView):
#     model = Student
#     fields = ['name', 'email', 'password']
#     success_url = '/updatethanks/'

#      # this function help us to make a class in label for applying css
#     def get_form(self):
#         form = super().get_form()
#         form.fields['name'].widget = forms.TextInput(attrs={'class' : 'myName'})
#         form.fields['email'].widget = forms.EmailInput(attrs={'class' : 'myEmail'})
#         form.fields['password'].widget = forms.PasswordInput(attrs={'class' : 'myPassword'})
#         return form

# class StudentUpdateTemplateView(TemplateView):
#     template_name = 'app1/updatethanks.html'


# ============================================================================================================

# Another way to apply css after given a class name.. You just go forms.py file and see

class StudentCreateView(CreateView):
    form_class = StudentModelForm
    template_name = 'app1/student_form.html'
    success_url = '/thanks/'


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    template_name = 'app1/student_form.html'
    success_url = '/updatethanks/'



class ThanksTemplateView(TemplateView):
    template_name = 'app1/thanks.html'



class StudentUpdateTemplateView(TemplateView):
    template_name = 'app1/updatethanks.html'
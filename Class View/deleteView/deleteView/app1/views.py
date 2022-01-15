from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from .models import Student
from django import forms
from .forms import StudentModelForm



class StudentCreateView(CreateView):
    form_class = StudentModelForm
    template_name = 'app1/student_form.html'
    success_url = '/thanks/'

class ThanksTemplateView(TemplateView):
    template_name = 'app1/thanks.html'



class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    template_name = 'app1/student_form.html'
    success_url = '/updatethanks/'


class StudentUpdateTemplateView(TemplateView):
    template_name = 'app1/updatethanks.html'


# class StudentDeleteView(DeleteView):
#     model = Student
#     success_url = '/'
#     # By default DeleteView demand the student_confirm_delete.html file. But we can also use our custom template
#     # Another thing is that in student_confirm_delete first student name came from the model name

class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/delete/'
    template_name = 'app1/delete.html'

class StudentDeleteTemplateView(TemplateView):
    template_name = 'app1/deletethanks.html'
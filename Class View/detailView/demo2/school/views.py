from django.shortcuts import render
from .models import Student
from django.views.generic.detail import DetailView

# Create your views here.
class StudentDetailView(DetailView):
    model = Student
    # If we want to change the default name
    template_name = 'school/student.html'
    # If we want to change the default context name
    context_object_name = 'stu' # now change it to html code
    # if we want to change default int:pk to int:id then
    pk_url_kwarg = 'id'
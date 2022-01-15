import imp
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Teacher, Student

# Create your views here.
class HomeListView(ListView):
    model = Teacher # model you have to specify otherwise you will get error
    template_name = 'app1/index.html'
    context_object_name = 'all_objects'
    # template_name_suffix = '_get'
    ordering = ['name']

    # it will return the filter queryset only

    # def get_queryset(self):
    #     return Teacher.objects.filter(course='Python')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["stu_objects"] = Student.objects.all() 
        return context
    

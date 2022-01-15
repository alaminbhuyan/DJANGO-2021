import imp
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Teacher, Student

# Create your views here.
class HomeDetailView(DetailView):
    model = Teacher
    template_name = 'app1/home.html'
    context_object_name = 'all_objects'

    # Pass all data together and pass multiple models objects
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["teacher_objects"] = self.model.objects.all()
        context["student_objects"] = Student.objects.all()
        return context
    
import imp
from django.contrib import admin
from .models import Teacher, Student


# Register your models here.
@admin.register(Teacher)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'course']


@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'course']
from django.contrib import admin
from .models import Teacher, Student


# Register your models here.

@admin.register(Teacher)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'take_subject')


@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'stu_ID', 'course')
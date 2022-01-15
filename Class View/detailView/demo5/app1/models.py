from pyexpat import model
from statistics import mode
from django.db import models



# Create your models here.
class Teacher(models.Model):
    name = models.CharField(verbose_name='Teacher_Name', max_length=60)
    email = models.EmailField(verbose_name='Teacher_email')
    take_subject = models.CharField(verbose_name='Subject_name', max_length=50)

class Student(models.Model):
    name = models.CharField(verbose_name='Student_Name', max_length=60)
    stu_ID = models.CharField(verbose_name='Student_ID', max_length=15)
    course = models.CharField(verbose_name='Course_name', max_length=50)
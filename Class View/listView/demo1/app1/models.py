from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    course = models.CharField(max_length=70)


class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    course = models.CharField(max_length=70)
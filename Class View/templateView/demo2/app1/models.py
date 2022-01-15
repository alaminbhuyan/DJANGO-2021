from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=40)
    roll = models.IntegerField()
    subject = models.CharField(max_length=50)
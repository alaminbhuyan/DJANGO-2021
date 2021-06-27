from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Status(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    status_publish_date = models.DateField()
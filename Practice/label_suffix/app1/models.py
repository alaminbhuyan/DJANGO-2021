from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
# Create your models here.
class Mobile(models.Model):
    name = models.CharField(max_length=100)
    brandName = models.CharField(max_length=100)
    modelName = models.CharField(max_length=40)
    price = models.FloatField()


class Computer(models.Model):
    processor = models.CharField(max_length=60)
    motherboard = models.CharField(max_length=80)
    powerSupply = models.CharField(max_length=70)
    caseing = models.CharField(max_length=70)
    ram = models.CharField(max_length=60)
    total_price = models.FloatField()


class UserProfile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="userImg")

class UserProfile2(models.Model):
    photo = models.ImageField(upload_to="userImg")
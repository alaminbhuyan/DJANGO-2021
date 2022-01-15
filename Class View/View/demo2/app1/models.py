from django.db import models



# Create your models here.
class UserSignUp(models.Model):
    username = models.CharField(verbose_name='userName', max_length=50)
    firstName = models.CharField(verbose_name='firstName', max_length=50)
    lastName = models.CharField(verbose_name='lastName', max_length=50)
    email = models.EmailField(verbose_name='userEmail', max_length=50)
    password1 = models.CharField(verbose_name='password', max_length=50)
    password2 = models.CharField(verbose_name='confirmPassword', max_length=50)
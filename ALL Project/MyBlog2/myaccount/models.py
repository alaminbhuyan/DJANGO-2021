from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class EveryUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_profile_image = models.ImageField(verbose_name="Your profile image",upload_to='profileImages', default="avater.png")
    token = models.CharField(verbose_name="Profile Token", max_length=150)
    verify = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
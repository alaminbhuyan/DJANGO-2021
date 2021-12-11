from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class EveryUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_profile_image = models.ImageField(upload_to='profile_images', default="avater.png")
    created_time = models.DateTimeField(auto_now_add=True)
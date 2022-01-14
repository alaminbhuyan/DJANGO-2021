from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class EveryUserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile')
    user_profile_image = models.ImageField(verbose_name="Your profile image",upload_to='profileImages', default="avater.png")
    token = models.CharField(verbose_name="Profile Token", max_length=150)
    forgetPasswordToken = models.CharField("ForgetPasswordToken", max_length=150)
    verify = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)

    # comment: User Profile Image resize Function
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.user_profile_image.path)
        if img.height > 300 or img.width > 300:
            output_size = (210, 210)
            img.thumbnail(size=output_size)
            img.save(self.user_profile_image.path)
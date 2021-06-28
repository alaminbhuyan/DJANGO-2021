from django.db import models
from django.utils.timezone import now
# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to="AllImages")
    date = models.DateTimeField(default=now)

from django.db import models
from django.urls import reverse
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    # Here "thanks" is came from urls.py name="thanks"
    # def get_absolute_url(self):
    #     return reverse("thanks")

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    
    
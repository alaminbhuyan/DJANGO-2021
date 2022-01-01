from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = tinymce_models.HTMLField()

    def __str__(self):
        return self.title
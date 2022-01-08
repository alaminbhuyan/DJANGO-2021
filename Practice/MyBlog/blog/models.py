from django.db import models
from tinymce import models as tinymce_models
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    post_created = models.DateTimeField(default=now)
    last_update = models.DateTimeField(auto_now=True)
    text = tinymce_models.HTMLField()

    def __str__(self):
        return self.title


class Atricals(models.Model):
    title = models.CharField(verbose_name="Title", max_length=100)
    artical_created = models.DateField(auto_now_add=True)
    artical_updated = models.DateTimeField(auto_now=True)
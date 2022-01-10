from django.db import models
from tinymce import models as tinymce_models



# Create your models here.

# class PythonBlogPost(models.Model):
#     title = models.CharField(verbose_name="Title", max_length=150)
#     description = models.CharField(verbose_name="Description", max_length=250)
#     post_created = models.DateField(verbose_name="Date", auto_now_add=True)
#     post_last_updated = models.DateTimeField(verbose_name="DateTime", auto_now=True)
#     text = tinymce_models.HTMLField()
#------------------------------------------------------------------------------------------

# Base class
class CommonInfo(models.Model):
    title = models.CharField(verbose_name="Title", max_length=150)
    description = models.CharField(verbose_name="Description", max_length=250)
    post_created = models.DateField(verbose_name="Date", auto_now_add=True)
    post_last_updated = models.DateTimeField(verbose_name="DateTime", auto_now=True)
    text = models.TextField(verbose_name="Enter your text")

    class Meta():
        abstract = True

# For Python blog post
# class PythonBlogPost(CommonInfo):
#     class Meta():
#         verbose_name_plural = 'PythonBlogPosts'
#         verbose_name = 'PythonBlogPost'
    
#     file = models.FileField(blank=True, null=True, upload_to="pythonFiles")

class PythonBlogPost(models.Model):
    title = models.CharField(verbose_name="Title", max_length=150)
    description = models.CharField(verbose_name="Description", max_length=250)
    post_created = models.DateField(verbose_name="Date", auto_now_add=True)
    post_last_updated = models.DateTimeField(verbose_name="DateTime", auto_now=True)
    text = models.TextField(verbose_name="Enter your text")


# For Django blog post
class DjangoBlogPost(CommonInfo):
    class Meta():
        verbose_name_plural = 'DjangoBlogPosts'
        verbose_name = 'DjangoBlogPost'
    
    file = models.FileField(blank=True, null=True, upload_to="djangoFiles")
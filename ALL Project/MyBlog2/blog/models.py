from django.db import models
from tinymce import models as tinymce_models
from django.contrib.auth.models import User


# Create your models here.

# class PythonBlogPost(models.Model):
#     title = models.CharField(verbose_name="Title", max_length=150)
#     description = models.CharField(verbose_name="Description", max_length=250)
#     post_created = models.DateField(verbose_name="Date", auto_now_add=True)
#     post_last_updated = models.DateTimeField(verbose_name="DateTime", auto_now=True)
#     text = tinymce_models.HTMLField()
# ------------------------------------------------------------------------------------------

# Base class
class CommonInfo(models.Model):
    title = models.CharField(verbose_name="Title", max_length=150)
    description = models.CharField(verbose_name="Description", max_length=250)
    post_created = models.DateField(verbose_name="Date", auto_now_add=True)
    post_last_updated = models.DateTimeField(
        verbose_name="DateTime", auto_now=True)
    text = models.TextField(verbose_name="Enter your text")

    class Meta():
        abstract = True

# For Python blog post


class PythonBlogPost(CommonInfo):

    class Meta():
        verbose_name_plural = 'PythonBlogPosts'
        verbose_name = 'PythonBlogPost'

    file = models.FileField(blank=True, null=True, upload_to="pythonFiles")


# For Django blog post
class DjangoBlogPost(CommonInfo):

    class Meta():
        verbose_name_plural = 'DjangoBlogPosts'
        verbose_name = 'DjangoBlogPost'

    file = models.FileField(blank=True, null=True, upload_to="djangoFiles")


# For ML blog post
class MLBlogPost(CommonInfo):

    class Meta():
        verbose_name_plural = 'MLBlogPosts'
        verbose_name = 'MLBlogPost'

    file = models.FileField(blank=True, null=True, upload_to="MLFiles")


# For DL blog post
class DLBlogPost(CommonInfo):

    class Meta():
        verbose_name_plural = 'DLBlogPosts'
        verbose_name = 'DLBlogPost'

    file = models.FileField(blank=True, null=True, upload_to="DLFiles")

#     @property
#     def file_exists(self):
#         # Because sometimes, the field may contain the string path
#         # but the file doesn't exist at all in the server
#         if self.file: # if the string path exists
#             return self.file.storage.exists(self.file.name) # If the file exists in server

    # @property
    # def file_exists(self):
    #     try:
    #         with open(self.file.path):
    #             return True
    #     except Exception:
    #         return False


# For about-us page
class AboutUs(models.Model):
    class Meta(object):
        verbose_name_plural = 'AboutUs'
        verbose_name = 'AboutUs'
    
    header = models.CharField(verbose_name="Title", max_length=100)
    text = models.TextField(verbose_name="Enter your text")


class Contact(models.Model):
    class Meta(object):
        verbose_name_plural = "Contacts"
        verbose_name = "Contact"
    
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Your name", max_length=70)
    email = models.EmailField(verbose_name="You Email")
    message = models.TextField(verbose_name="Your Message")
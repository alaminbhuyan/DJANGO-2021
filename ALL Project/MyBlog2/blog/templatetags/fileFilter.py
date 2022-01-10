from django import template
from django.core.files.storage import default_storage
import os

register = template.Library()

@register.filter(name="check_fileExist_or_not")
def checkFileExitsOrNot(filepath):
    if default_storage.exists(name=filepath):
        return filepath
    # else:
    #     index = filepath.rfind('/')
    #     new_filepath = filepath[:index] + '/image.png'
    #     return new_filepath
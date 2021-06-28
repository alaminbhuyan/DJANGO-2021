from django import forms
from .models import Image

# You can write your class from here

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['photo']
        labels = {'photo':""}
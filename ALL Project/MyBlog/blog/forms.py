from django import forms
from .models import PythonBlogPost, DjangoBlogPost

class PythonBlogAdminForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))

    class Meta(object):
        model = PythonBlogPost
        fields = "__all__"

class DjangoBlogAdminForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))
    
    class Meta(object):
        model = DjangoBlogPost
        fields = "__all__"
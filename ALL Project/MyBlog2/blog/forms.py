from django import forms
from .models import (PythonBlogPost, DjangoBlogPost,
 MLBlogPost, DLBlogPost, AboutUs, Contact)



class PythonBlogAdminForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))
    # file = forms.FileField(required=False,widget=forms.ClearableFileInput(attrs={'multiple' : True}))
    file = forms.FileField(required=False,widget=forms.FileInput(attrs={'multiple' : True}))


    class Meta(object):
        model = PythonBlogPost
        fields = "__all__"

class DjangoBlogAdminForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))
    
    class Meta(object):
        model = DjangoBlogPost
        fields = "__all__"


class MLBlogAdminForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))
    
    class Meta(object):
        model = MLBlogPost
        fields = "__all__"

class DLBlogAdminForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))
    
    class Meta(object):
        model = DLBlogPost
        fields = "__all__"


class AboutUsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))
    
    class Meta(object):
        model = AboutUs
        fields = "__all__"


class ContactModelForm(forms.ModelForm):
    name = forms.CharField(max_length=70, required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'*Name...'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'*Email...'}))
    message = forms.CharField(max_length=250, required=True, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'*Message...', 'rows':10}))

    class Meta(object):
        model = Contact
        fields = "__all__"
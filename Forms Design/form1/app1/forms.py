from django import forms
from django.core import validators
import re
import string



# Custom form validators
# comment: for UserName
def checkPunctuation(value):
    if re.search(pattern='[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]', string=value):
        raise forms.ValidationError(message="UserName can't contain any Punctuation")

def checkSpace(value):
    if ' ' in value:
        raise forms.ValidationError(message="UserName can't contain any space")

def checkOnlyDigits(value):
    if value.isdigit():
        raise forms.ValidationError(message="UserName can't contain Only digits")

def checkOnlyDigits_fn(value):
    if value.isdigit():
        raise forms.ValidationError(message="FirstName can't contain Only digits")

def checkAnyDigits_fn2(value):
    if re.search(pattern="\d", string=value):
        raise forms.ValidationError(message="FirstName can't contain any digits")

def checkOnlyDigits_ln(value):
    if value.isdigit():
        raise forms.ValidationError(message="LastName can't contain Only digits")

def checkAnyDigits_ln2(value):
    if re.search(pattern="\d", string=value):
        raise forms.ValidationError(message="LastName can't contain any digits")

class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'UserName'}), error_messages={'required':'Enter Your UserName'}, validators=[checkSpace, checkOnlyDigits,checkPunctuation])

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'FirstName'}), error_messages={'required':'Enter Your First Name'}, validators=[checkOnlyDigits_fn,checkAnyDigits_fn2])

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'LastName'}), error_messages={'required':'Enter Your Last Name'}, validators=[checkOnlyDigits_ln,checkAnyDigits_ln2])

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder' : 'Email'}), error_messages={'required':'Enter Your Email'})

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}), error_messages={'required':'Enter Your Password'}, validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(30)])

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}), label="Confirm Password:", error_messages={'required':'Enter Your Confirm Password'}, validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(30)])

    # comment: apply some restriction my own will
    # def clean_password(self):
    #     pass1 = self.changed_data['password']
    #     pass2 = self.changed_data['password2']
    #     if pass1 != pass2:
    #         raise forms.ValidationError(message="Your Password not Match")
    def clean(self):
        cleaned_data = super().clean()
        try:
            pass1 = cleaned_data['password']
            pass2 = cleaned_data['password2']
            # if pass1 != pass2:
            #     raise forms.ValidationError(message="Your Password not Match")
        except KeyError:
            pass
        else:
            pass1 = cleaned_data['password']
            pass2 = cleaned_data['password2']
            if pass1 != pass2:
                raise forms.ValidationError(message="Your Password not Match")


class UserForm2(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'UserName'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'FirstName'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'LastName'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder' : 'Email'}))

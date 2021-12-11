# If we want to show more fields in webpage then use this technique

# comment: By-Default in 'UserCreationForm' have three fields
#   1) UserName 2) Password 3) Confirm Password (password2)

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import (authenticate, get_user_model, password_validation)
from django.utils.translation import gettext, gettext_lazy as _
from .models import EveryUserProfile
from django.core import validators
from django import forms
import string
import re

# ===============================================================================================
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
# ===============================================================================================

# We just extend form to User form
class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Username'}), help_text='Required',error_messages={'required' : 'Enter your UserName'}, validators=[checkSpace, checkOnlyDigits,checkPunctuation])

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your FirstName'}), help_text='Required',error_messages={'required' : 'Enter your First Name'}, validators=[checkOnlyDigits_fn,checkAnyDigits_fn2])

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your LastName'}), help_text='Required',error_messages={'required' : 'Enter your Last Name'}, validators=[checkOnlyDigits_ln,checkAnyDigits_ln2])

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your Vaild Email'}),help_text='Required',error_messages={'required' : 'Enter your Email'})

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter your password'}), label="Password:",error_messages={'required' : 'Enter your Password'}, validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(30)])

    password2 = forms.CharField(label='Confirm Password (Again)', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Re-enter your password'}),error_messages={'required' : 'Enter your Password'}, validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(30)])

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email' : "Email"}
        # widgets = {
        #     'username' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Username'}),
        # }

# Comment: By-default 'UserChangeForm' return the Admin full forms. So, we just select the necessary fields only
class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        # fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login', 'is_active']
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email' : 'Email'}
        error_messages = {
            'first_name' : {'required' : 'Enter Your First Name'},
            'last_name' : {'required' : 'Enter Your Last Name'},
            'email' : {'required' : 'Enter Your Email'},
        }
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Username'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your FirstName'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your LastName'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your Valid Email'}),
            'date_joined' : forms.TextInput(attrs={'class':'form-control'}),
            'last_login' : forms.TextInput(attrs={'class':'form-control'}),
            'is_active' : forms.CheckboxInput(attrs={'class':"form-check-input"}),
        }

# comment: Overwrite the AuthenticationForm for apply css
class MyAuthenticationForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control', 'placeholder':'Enter your Username'}),error_messages={'required':'Enter Your UserName'})
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control', 'placeholder':'Enter your password'}),error_messages={'required':'Enter Your Password'})


# comment: Overwrite the PasswordChangeForm for apply css
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, 'class':'form-control','placeholder':'Enter your Old password'}), error_messages={'required':'Enter Your Old Password'})
    
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control','placeholder':'Enter your Old password'}), error_messages={'required':'Enter Your New Password'},
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control','placeholder':'Enter your Old password'}), error_messages={'required':'Re-Enter Your New Password'},
    )


# For user upload user profile picture
class EveryUserProfileForm(forms.ModelForm):
    class Meta(object):
        model = EveryUserProfile
        fields = ['user_profile_image']
        labels = {'user_profile_image' : 'Profile-Image:'}


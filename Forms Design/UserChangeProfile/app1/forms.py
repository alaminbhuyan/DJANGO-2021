# If we want to show more fields in webpage then use this technique

# comment: By-Default in 'UserCreationForm' have three fields
#   1) UserName 2) Password 3) Confirm Password (password2)

from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _
from django.db import models
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)


# We just extend form to User form
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter your password'}), label="Password:")
    password2 = forms.CharField(label='Confirm Password (Again)', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Re-enter your password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email' : "Email"}
        error_messages = {
            'first_name' : {'required' : 'Enter Your First Name'},
            'last_name' : {'required' : 'Enter Your Last Name'},
            'email' : {'required' : 'Enter Your Email'},
        }
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Username'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your FirstName'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your LastName'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your Vaild Email'}),
        }

# Comment: By-default 'UserChangeForm' return the Admin full forms. So, we just select the necessary fields only
class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login', 'is_active']
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
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your Vaild Email'}),
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
        

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

# By default UserCreationForm gives us only three fields. So we want more field like
# username, first_name, last_name, email. so we extend those field from User models

class SignUpForm(UserCreationForm):
    # here password2 means 'Password confirmation'
    password2 = forms.CharField(label="Confirm Password (again)",widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {"email":"Email"}


class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        # fields = ['username','first_name','last_name','email','date_joined','last_login','is_active']
        fields = ['username','first_name','last_name','email','date_joined','last_login']
        labels = {'email':'Email'}


class EditAdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = "__all__"
        labels = {'email':'Email'}
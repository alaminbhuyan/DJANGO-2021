# If we want to show more fields in webpage then use this technique
# comment: By-Default in 'UserCreationForm' have three fields
#   1) UserName 2) Password 3) Confirm Password (password2)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# We just extend form to User form
class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (Again)', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email' : "Email"}
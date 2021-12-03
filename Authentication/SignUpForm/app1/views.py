from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages


# Create your views here.
# This lines of code only show in webpage Username, Password, ConfirmPassword
# def signUp(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = UserCreationForm()
#     return render(request=request, template_name='app1/signup.html', context={'form' : form})


def signUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request=request, message="Account Created Successfully!!!")
            form.save()
    else:
        form = SignUpForm()
    return render(request=request, template_name='app1/signup.html', context={'form' : form})
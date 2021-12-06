from django import forms
from django.shortcuts import render
from .forms import UserForm, UserForm2
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
                print("form validated")
                print("UserName: ", form.cleaned_data['username'])
                print("FirstName: ", form.cleaned_data['first_name'])
                print("LastName: ", form.cleaned_data['last_name'])
                print("Email: ", form.cleaned_data['email'])
                print("Password: ", form.cleaned_data['password'])
                print("Password2: ", form.cleaned_data['password2'])
    else:
        form = UserForm()
    return render(request=request, template_name='app1/userForm.html', context={'form' : form})

def home2(request):
    if request.method == 'POST':
        form = UserForm2(data=request.POST)
        if form.is_valid():
            print("form validated")
            print("UserName: ", form.cleaned_data['username'])
            print("FirstName: ", form.cleaned_data['first_name'])
            print("LastName: ", form.cleaned_data['last_name'])
            print("Email: ", form.cleaned_data['email'])
    else:
        form = UserForm2()
    return render(request=request, template_name='app1/home2.html', context={'form' : form})



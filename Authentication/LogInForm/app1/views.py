from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Signup form function
def signUp(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request=request, message="Account Created Successfully!!!")
                form.save()
        else:
            form = SignUpForm()
        return render(request=request, template_name='app1/signup.html', context={'form' : form})
    else:
        return HttpResponseRedirect(redirect_to='/profile/')

# Login form function
def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_password = form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_password)
                if user is not None:
                    login(request=request, user=user)
                    messages.success(request=request, message="LogIn successfully!!")
                    return HttpResponseRedirect(redirect_to='/profile/')
        else:
            form = AuthenticationForm()
        return render(request=request, template_name="app1/userLogin.html", context={'form' : form})
    else:
        return HttpResponseRedirect(redirect_to='/profile/')

# Profile page function
def userProfile(request):
    if request.user.is_authenticated:
        return render(request=request, template_name="app1/profile.html", context={'name' : request.user})
    else:
        return HttpResponseRedirect(redirect_to='/login/')


# Logout form function
def userLogout(request):
    logout(request=request)
    return HttpResponseRedirect(redirect_to='/login/')
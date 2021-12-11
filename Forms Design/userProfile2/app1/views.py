from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import (SignUpForm, EditUserProfileForm, 
MyAuthenticationForm, MyPasswordChangeForm, EveryUserProfileForm)

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash



# Home function
def home(request):
    return render(request=request, template_name="app1/home.html")


# Signup form function
def signUp(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                check_email = form.cleaned_data.get('email')
                user_obj = User.objects.filter(email=check_email).first()
                if user_obj:
                    messages.error(request=request, message="This Email already Taken. Try with different valid Email....!")
                    return HttpResponseRedirect(redirect_to='/signup/')
                messages.success(request=request, message="Account Created Successfully!!!")
                form.save()
                return HttpResponseRedirect(redirect_to='/login/')
        else:
            form = SignUpForm()
        return render(request=request, template_name='app1/signup.html', context={'form' : form})
    else:
        return HttpResponseRedirect(redirect_to='/profile/')

# Login form function
def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = MyAuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_password = form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_password)
                if user is not None:
                    login(request=request, user=user)
                    messages.success(request=request, message="LogIn successfully!!")
                    return HttpResponseRedirect(redirect_to='/')
        else:
            form = MyAuthenticationForm()
        return render(request=request, template_name="app1/userLogin.html", context={'form' : form})
    else:
        return HttpResponseRedirect(redirect_to='/profile/')

# Profile page function
def userProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_form = EditUserProfileForm(data = request.POST, instance=request.user)
            profile_form = EveryUserProfileForm(data= request.POST, files=request.FILES, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                messages.success(request=request, message="Profile Updated")
                user_form.save()
                profile_form.save()
        else:
            user_form = EditUserProfileForm(instance=request.user)
            profile_form = EveryUserProfileForm(instance=request.user.profile)
        context = {
            'user_form' : user_form,
            'profile_form' : profile_form
        }
        return render(request=request, template_name="app1/profile.html", context=context)
    else:
        return HttpResponseRedirect(redirect_to='/login/')

# User change Password with old password
def userChangePassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MyPasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request=request, message="Password updated Successfully!!")
                update_session_auth_hash(request=request, user=form.user)
                return HttpResponseRedirect(redirect_to='/profile/')
        else:
            form = MyPasswordChangeForm(user=request.user)
        return render(request=request, template_name="app1/changepassword.html", context={'form' : form})
    else:
        return HttpResponseRedirect(redirect_to='/login/')



# Logout form function
def userLogout(request):
    logout(request=request)
    messages.success(request=request, message="LogOut Successfully!!")
    return HttpResponseRedirect(redirect_to='/login/')


def deleteConfirmation(request):
    return render(request=request, template_name="app1/deleteConfirmation.html")


def deleteAccount(request, email):
    user_email = User.objects.get(email=email)
    if user_email:
        messages.success(request=request, message="User Profile Deleted Successfully")
        user_email.delete()
        return HttpResponseRedirect(redirect_to='/')
    return HttpResponse("Error: Something is wrong")
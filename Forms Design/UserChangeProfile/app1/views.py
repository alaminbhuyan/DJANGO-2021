from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, EditUserProfileForm, MyAuthenticationForm, MyPasswordChangeForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

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
            form = MyAuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_password = form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_password)
                if user is not None:
                    login(request=request, user=user)
                    messages.success(request=request, message="LogIn successfully!!")
                    return HttpResponseRedirect(redirect_to='/profile/')
        else:
            form = MyAuthenticationForm()
        return render(request=request, template_name="app1/userLogin.html", context={'form' : form})
    else:
        return HttpResponseRedirect(redirect_to='/profile/')

# Profile page function
def userProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditUserProfileForm(data = request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request=request, message="Profile Updated")
                form.save()
        else:
            form = EditUserProfileForm(instance=request.user)
        return render(request=request, template_name="app1/profile.html", context={'name' : request.user, 'form': form})
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

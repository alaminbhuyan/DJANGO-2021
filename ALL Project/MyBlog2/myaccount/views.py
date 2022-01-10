from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import EveryUserProfile
from .tokens import send_email_after_registration
from django.views import View
from .forms import (SignUpForm, EditUserProfileForm, 
MyAuthenticationForm, MyPasswordChangeForm, EveryUserProfileForm)
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
import uuid
from blog.models import Contact

# Create your views here.

# Comment: SignUp Function
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(data=request.POST)
            if form.is_valid():
                check_email = form.cleaned_data['email']
                user_obj = User.objects.filter(email=check_email).first()
                if user_obj:
                    messages.error(request=request, message="This Email already Taken. Try with different valid Email....!")
                    return HttpResponseRedirect(redirect_to='/myaccount/signup')
                new_user = form.save()
                uid = uuid.uuid4()
                profile_object = EveryUserProfile(user=new_user, token=uid)
                profile_object.save()
                messages.success(
                request, "One email send to Your Email Address, Check your Email and Verify Your Account")
                send_email_after_registration(email=new_user.email, token=uid)
                return HttpResponseRedirect(redirect_to='/myaccount/signin/')
        else:
            form = SignUpForm()
        return render(request=request, template_name='myaccount/signup.html', context={'form': form})
    else:
        return HttpResponseRedirect(redirect_to='/myaccount/profile/')

# Comment: LogIn Function
def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = MyAuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                pro = EveryUserProfile.objects.get(user=user)

                if pro.verify:
                    login(request=request, user=user)
                    # messages.success(request=request, message="Login Successfully!")
                    return HttpResponseRedirect(redirect_to='/')
                else:
                    messages.error(request=request, message="Your account is not verified, please check your email and verify your Account")
                    return HttpResponseRedirect(redirect_to='/myaccount/signin/')
        else:
            form = MyAuthenticationForm()
        return render(request=request, template_name='myaccount/userLogin.html', context={'form': form})
    else:
        return HttpResponseRedirect(redirect_to='/myaccount/profile/')

# Comment: Account Verify Function
def account_verify(request, token):
    pf = EveryUserProfile.objects.filter(token=token).first()
    if pf.verify:
        messages.success(request, "Your account already verified. Don't need to verify again!")
        return HttpResponseRedirect(redirect_to='/myaccount/signin/')
    else:
        pf.verify = True
        pf.save()
        messages.success(request, "Your account has been verified, You can login!")
        return HttpResponseRedirect(redirect_to='/myaccount/signin/')

# Comment: User Profile Function
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_form = EditUserProfileForm(data = request.POST, instance=request.user)
            profile_form = EveryUserProfileForm(data= request.POST, files=request.FILES, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                messages.success(request=request, message="Profile Updated Successfully")
                user_form.save()
                profile_form.save()
        else:
            user_form = EditUserProfileForm(instance=request.user)
            profile_form = EveryUserProfileForm(instance=request.user.profile)
        context = {
            'user_form' : user_form,
            'profile_form' : profile_form
        }
        return render(request=request, template_name="myaccount/profile.html", context=context)
    else:
        return HttpResponseRedirect(redirect_to='/myaccount/signin/')


# User change Password with old password
def userChangePassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MyPasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request=request, message="Password updated Successfully!!")
                update_session_auth_hash(request=request, user=form.user)
                return HttpResponseRedirect(redirect_to='/myaccount/profile/')
        else:
            form = MyPasswordChangeForm(user=request.user)
        return render(request=request, template_name="myaccount/changepassword.html", context={'form' : form})
    else:
        return HttpResponseRedirect(redirect_to='/myaccount/signin/')


# Comment: User Delete Confirmation Function
def deleteConfirmation(request):
    return render(request=request, template_name="myaccount/deleteConfirmation.html")

# Comment: User Delete Function
def deleteAccount(request, email):
    user_email = User.objects.get(email=email)
    deleteContact(email)
    if user_email:
        messages.success(request=request, message="User Profile Deleted Successfully")
        user_email.delete()
        return HttpResponseRedirect(redirect_to='/myaccount/signup')
    return HttpResponse("Error: Something is wrong")


def deleteContact(email):
    try:
        contact_email = Contact.objects.get(email=email)
    except:
        pass
    else:
        contact_email.delete()

# Comment: User LogOut Function
def accountLogout(request):
    logout(request=request)
    return HttpResponseRedirect(redirect_to='/myaccount/signin/')
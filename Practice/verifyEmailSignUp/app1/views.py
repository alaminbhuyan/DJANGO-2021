import django
from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import SignUpForm
from .models import Profile
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import uuid
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def send_email_after_registration(email, token):
    subject = "Verify Your Email"
    message = f"Hi, Click on the link to verify your account http://127.0.0.1:8000/account-verify/{token}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            uid = uuid.uuid4()
            profile_object = Profile(user=new_user, token=uid)
            profile_object.save()
            messages.success(request, "One email send to your email, check your email and verify your account")
            send_email_after_registration(email=new_user.email, token=uid)
    else:
        form = SignUpForm()
    return render(request, 'app1/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            pro = Profile.objects.get(user=user)

            if pro.verify:
                login(request=request, user=user)
                # messages.success(request=request, message="Login Successfully!")
                return redirect('profile')
            else:
                messages.info(request=request, message="Your account is not verified, please check your email and verify your Account")
                return redirect('/signin/')
    else:
        form = AuthenticationForm()
    return render(request, 'app1/login.html', {'form': form})

def account_verify(request, token):
    pf = Profile.objects.filter(token=token).first()
    if pf.verify:
        messages.success(request, "Your account already verified. Don't need to verify again!")
        return redirect('/signin/')
    else:
        pf.verify = True
        pf.save()
        messages.success(request, "Your account has been verified, You can login!")
        return redirect('/signin/')

def profile(request):
    return render(request=request, template_name="app1/profile.html")

def accountLogout(request):
    logout(request)
    return redirect('/signin/')
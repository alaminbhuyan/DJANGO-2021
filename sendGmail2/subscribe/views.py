from django.shortcuts import render
# from sendGmail2.settings import EMAIL_HOST_USER
from django.conf import settings
from . import forms
from django.core.mail import send_mail

# Create your views here.

# def subscribe(request):
#     sub = forms.Subscribe()
#     if request.method == "POST":
#         sub = forms.Subscribe(request.POST)
#         subject = "Welcome to DataFlair"
#         message = "Hope you are enjoying your django Project"
#         recepient = str(sub['email'].value())
#         x = sub['email'].value()
#         print(x)
#         # send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently= False)
#         return render(request, 'subscribe/success.html', context={'recepient':recepient})

#     return render(request, "subscribe/index.html", context={'form':sub})

def subscribe(request):
    sub = forms.Subscribe()
    if request.method == "POST":
        sub = forms.Subscribe(request.POST)
        subject = 'Your accounts need to be verified'
        message = f'Hi paste the link to verify your account'
        email = str(sub['email'].value())
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message , email_from ,recipient_list )
        return render(request, 'subscribe/success.html', context={'recepient':email})

    return render(request, "subscribe/index.html", context={'form':sub})




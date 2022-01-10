from django.core.mail import send_mail
from django.conf import settings


def send_email_after_registration(email, token):
    subject = "Verify Your Email"
    message = f"Hi, Click on the link to verify your account http://127.0.0.1:8000/myaccount/account-verify/{token}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)

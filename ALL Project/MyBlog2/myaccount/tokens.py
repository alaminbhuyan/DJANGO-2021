from django.core.mail import send_mail
from django.conf import settings

# comment: For Signup Email verification
def send_email_after_registration(email, token):
    subject = "Verify Your Email"
    message = f"Hi, Click on the link to verify your account http://127.0.0.1:8000/myaccount/account-verify/{token}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)


# comment: For Forgot password Email verification
def setForgotPassword(email, token):
    subject = "Your forgot password link"
    message = f"Hi, Click on the link to reset your password http://127.0.0.1:8000/myaccount/setNewPassword/{token}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)
    return True

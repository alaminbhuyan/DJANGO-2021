from django.core.mail import EmailMessage, send_mail
from django.conf import settings
import os


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['subject'],
            body=data['body'],
            from_email=os.environ.get('EMAIL_FROM'),
            to=[data['to_email']]
        )
        email.send()

# def send_email(email, link):
#     subject = "Reset Your Password"
#     message = f"Click Following Link to Reset Your Password {link}"
#     from_email = settings.EMAIL_HOST_USER
#     recipient_list = [email]
#     send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)


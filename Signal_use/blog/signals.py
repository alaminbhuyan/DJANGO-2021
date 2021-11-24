from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver

@receiver(signal=user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("-------------------------------------")
    print("Logged-in Signal.....Run Intro...")
    print("Sender: ", sender)
    print("Request: ", request)
    print("User: ", user)
    print(f'kwargs: {kwargs}')

# user_logged_in.connect(receiver=login_success, sender=User)


@receiver(signal=user_logged_out, sender=User)
def login_success(sender, request, user, **kwargs):
    print("-------------------------------------")
    print("Logged-Out Signal.....Run Intro...")
    print("Sender: ", sender)
    print("Request: ", request)
    print("User: ", user)
    print(f'kwargs: {kwargs}')



@receiver(signal=user_login_failed)
def login_success(sender, credentials, request, **kwargs):
    print("-------------------------------------")
    print("Logged-in-failed Signal......")
    print("Sender: ", sender)
    print("Credentials: ",credentials)
    print("Request: ", request)
    print(f'kwargs: {kwargs}')
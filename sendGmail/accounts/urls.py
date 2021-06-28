from django.urls import path
from . import views

urlpatterns = [
    path(route='', view= views.home, name="home_page"),
    path(route='register', view=views.register_attempt, name="register_attempt"),
    path(route='accounts/login/', view=views.login_attempt, name="login_attempt"),
    path(route='token', view=views.token_send, name="token_send"),
    path(route='success', view=views.success, name="success"),
    path(route='verify/<authToken>', view=views.verify, name="verify"),
    path(route='error', view=views.error_page, name="error"),
]

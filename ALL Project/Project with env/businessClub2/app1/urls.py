from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.home, name='homepage'),
    path(route='registrationform/',view=views.registrationform, name='registrationform'),
    path(route='about/',view=views.about, name='aboutpage'),
    path(route='contact/',view=views.contact, name='contactpage'),
]

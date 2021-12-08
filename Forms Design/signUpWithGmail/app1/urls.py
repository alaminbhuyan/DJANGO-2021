from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.signup, name='signup'),
    path(route='activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', view=views.activate, name='activate'),
]

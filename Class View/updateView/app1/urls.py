from django.urls import path
from . import views


urlpatterns = [
    path(route='', view=views.StudentCreateView.as_view(), name='stucreate'),
    path(route='thanks/', view=views.ThanksTemplateView.as_view(), name='thanks'),
    path(route='stuupdate/<int:pk>', view=views.StudentUpdateView.as_view(), name='stuupdate'),
    path(route='updatethanks/', view=views.StudentUpdateTemplateView.as_view(), name='updatethanks'),
]

from django.urls import path
from . import views


urlpatterns = [
    path(route='', view=views.StudentCreateView.as_view(), name='stucreate'),
    path(route='thanks/', view=views.ThanksTemplateView.as_view(), name='thanks'),
]

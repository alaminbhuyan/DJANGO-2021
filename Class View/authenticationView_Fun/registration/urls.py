from django.urls import path, include
from . import views

urlpatterns = [
    path(route='accounts/', view=include('django.contrib.auth.urls')),
    path(route='accounts/profile/', view=views.profile, name='profile'),
    path(route='about/', view=views.about, name='about'),
    path(route='confidential/', view=views.confidential, name='confidential'),
]

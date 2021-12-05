from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required




urlpatterns = [
    path(route='accounts/', view=include('django.contrib.auth.urls')),

    path(route='accounts/profile/', view=views.ProfileTemplateView.as_view(), name='profile'),

    path(route='about/', view=views.AboutTemplateView.as_view(), name='about'),

    path(route='confidential/', view=views.ConfidentialTemplateView.as_view(), name='confidential'),

    ## This is one way

    # path(route='accounts/profile/', view=login_required(views.StudentTemplateView.as_view()), name='profile'),
    # path(route='about/', view=login_required(views.AboutTemplateView.as_view()), name='about'),
    # path(route='confidential/', view=staff_member_required(views.ConfidentialTemplateView.as_view()), name='confidential'),
]

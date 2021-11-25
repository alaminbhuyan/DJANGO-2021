from django.urls import path
from . import views


urlpatterns = [
    path(route='', view=views.ContactFormView.as_view(), name="contact"),
    path(route='thankyou/', view=views.ThanksTemplateView.as_view(), name="thankyou"),
]

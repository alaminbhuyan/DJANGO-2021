from django.urls import path
from . import views


urlpatterns = [
    # Direct access without write anything in view.py file
    path(route='', view=views.TemplateView.as_view(template_name="app1/home.html"),name="home_page"),

    # Without Direct access write something in view.py file
    path(route='about/', view=views.AboutTemplateView.as_view(), name="about_page"),

    # passing context
    path(route='profile/', view=views.ProfileTemplateView.as_view(extra_context={"course":"Python"}), name="profile_page"),

    path(route='information/<int:id>', view=views.InformationTemplateView.as_view(), name="information_page"),
]

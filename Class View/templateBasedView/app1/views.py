from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class AboutTemplateView(TemplateView):
    template_name = "app1/about.html"



# Pass context
class ProfileTemplateView(TemplateView):
    template_name = "app1/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Alamin"
        context["roll"] = 101
        return context


class InformationTemplateView(TemplateView):
    template_name = "app1/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Alamin"
        context["roll"] = 101

        print(kwargs)
        return context
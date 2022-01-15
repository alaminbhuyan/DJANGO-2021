from django.shortcuts import render, HttpResponse
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

# Create your views here.
class ContactFormView(FormView):
    template_name = 'school/contact.html'
    form_class = ContactForm
    success_url = "/thankyou/"
    initial = {'name' : 'alamin', 'email' : 'alaminbhuyan321@gmail.com'}
    def form_valid(self, form):
        print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['message'])
        return super().form_valid(form=form)
        # return HttpResponse("Your form is submited")



class ThanksTemplateView(TemplateView):
    template_name = 'school/thankyou.html'
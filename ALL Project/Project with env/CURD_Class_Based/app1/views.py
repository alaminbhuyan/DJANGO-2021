from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import StudentRegistration
from django.contrib import messages
from django.views.generic.base import TemplateView, View, RedirectView

# Create your views here.



class AddShowView(TemplateView):
    template_name = "app1/addAndShow.html"

    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args, **kwargs)
        fm = StudentRegistration()
        student_info = User.objects.all()
        context= {'form': fm, 'info':student_info}
        return context
    
    def post(self, request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            reg = User(name=name, email=email, password=password)
            reg.save()
            messages.success(request=request, message="You Successfully Add New Record")
            return HttpResponseRedirect('/')
#? This function add new record in the database

# def add_show(request):
#     if request.method == 'POST':
#         fm = StudentRegistration(request.POST)
#         if fm.is_valid():
#             name = fm.cleaned_data['name']
#             email = fm.cleaned_data['email']
#             password = fm.cleaned_data['password']
#             reg = User(name=name, email=email, password=password)
#             reg.save()
#             messages.success(request=request, message="You Successfully Add New Record")
#             fm = StudentRegistration()
#     else:
#         fm = StudentRegistration()

#     student_info = User.objects.all()
#     return render(request, "app1/addAndShow.html", context={'form': fm, 'info':student_info})









#? This function update the database record

# def update_data(request, id):
#     if request.method == "POST":
#         record = User.objects.get(pk=id)
#         fm = StudentRegistration(request.POST, instance=record)
#         if fm.is_valid():
#             fm.save()
#         messages.success(request=request, message="You Successfully Updated your Record")
#         return HttpResponseRedirect('/')
#     else:
#         record = User.objects.get(pk=id)
#         fm = StudentRegistration(instance=record)
#     return render(request, "app1/update.html", context={'form':fm})


class UpdateDataView(View):
    def get(self, request, id):
        record = User.objects.get(pk=id)
        fm = StudentRegistration(instance=record)
        return render(request, "app1/update.html", context={'form':fm})
    
    def post(self, request, id):
        record = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=record)
        if fm.is_valid():
            fm.save()
        messages.success(request=request, message="You Successfully Updated your Record")
        return HttpResponseRedirect('/')





#? This function delete the record in the database table

# def delete_data(request, id):
#     if request.method == "POST":
#         record = User.objects.get(pk=id)
#         record.delete()
#         messages.success(request=request, message="You Successfully Delete your Record")
#         return HttpResponseRedirect('/')

class DeleteDataView(RedirectView):
    url = '/' # after redirect it will come back home page
    def get_redirect_url(self, *args, **kwargs):
        delete_id = kwargs['id']
        User.objects.get(pk=delete_id).delete()
        return super().get_redirect_url(*args, **kwargs)
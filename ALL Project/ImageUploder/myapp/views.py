from django.shortcuts import render, HttpResponseRedirect
from .forms import ImageForm
from .models import Image

# Create your views here.
def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES) # request.FILES USE FOR IMAGE MANUPULATION
        if form.is_valid():
            form.save()
    else:
        form = ImageForm()
    
    img = Image.objects.all()

    return render(request=request, template_name="myapp/index.html", context={'form':form, 'img':img})


# delete data
def delete_data(request, id):
    if request.method == "POST":
        record = Image.objects.get(pk=id)
        record.delete()
        return HttpResponseRedirect('/')
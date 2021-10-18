from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


# Create your views here.

def home(request):
    all_post = Post.objects.all().order_by('id')
    # my_paginator = Paginator(object_list=all_post, per_page=3)
    my_paginator = Paginator(object_list=all_post, per_page=3, orphans=1)
    page_number = request.GET.get('page')
    page_obj = my_paginator.get_page(number=page_number)
    return render(request=request, template_name="blogs/home.html", context={"all_post":page_obj})
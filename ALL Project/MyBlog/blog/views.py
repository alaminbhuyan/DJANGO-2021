from django.db import models
from django.shortcuts import render
from django.http import Http404
from .models import PythonBlogPost, DjangoBlogPost
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

# Create your views here.

# def home(request):
#     return render(request=request, template_name="blog/home.html")

class HomeTemplateView(TemplateView):
    template_name = 'blog/home.html'


# def pythonBlog(request):
#     all_posts = PythonBlogPost.objects.all()
#     return render(request=request, template_name="blog/PythonBlogLink.html", context={'all_posts': all_posts})

class PythonBlogListView(ListView):
    model = PythonBlogPost
    template_name = 'blog/PythonBlogLink.html'
    context_object_name = "all_posts"
    # ordering = ['id']
    paginate_by = 10
    paginate_orphans = 1

    # handle Http-404 error
    def get_context_data(self, *args, **kwargs):
        try:
            return super(PythonBlogListView, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(PythonBlogListView, self).get_context_data(*args, **kwargs)


class PythonBlogDetailView(DetailView):
    model = PythonBlogPost
    template_name = 'blog/singlePost.html'
    context_object_name = "post"



class DjangoBlogListView(ListView):
    model = DjangoBlogPost
    template_name = 'blog/djangoBlogLink.html'
    context_object_name = "all_posts"
    paginate_by = 3
    paginate_orphans = 1

    # handle Http-404 error
    def get_context_data(self, *args, **kwargs):
        try:
            return super(DjangoBlogListView, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(DjangoBlogListView, self).get_context_data(*args, **kwargs)



def MLBlog(request):
    return render(request=request, template_name="blog/MLblogLink.html")


def DLBlog(request):
    return render(request=request, template_name="blog/DLblogLink.html")
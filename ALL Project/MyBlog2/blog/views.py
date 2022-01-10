from django.db import models
from django.shortcuts import render
from django.http import Http404
from .models import (PythonBlogPost, DjangoBlogPost,
 MLBlogPost, DLBlogPost, AboutUs)
from .forms import ContactModelForm
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
import random

# Create your views here.


class HomeTemplateView(TemplateView):
    template_name = 'blog/home.html'


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
    template_name = 'blog/pythonSinglePost.html'
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


class DjangoBlogDetailView(DetailView):
    model = DjangoBlogPost
    template_name = 'blog/djangoSinglePost.html'
    context_object_name = "post"


class MLBlogListView(ListView):
    model = MLBlogPost
    template_name = 'blog/MLblogLink.html'
    context_object_name = "all_posts"
    paginate_by = 3
    paginate_orphans = 1

    # handle Http-404 error
    def get_context_data(self, *args, **kwargs):
        try:
            return super(MLBlogListView, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(MLBlogListView, self).get_context_data(*args, **kwargs)


class MLBlogDetailView(DetailView):
    model = MLBlogPost
    template_name = 'blog/MLSinglePost.html'
    context_object_name = "post"


class DLBlogListView(ListView):
    model = DLBlogPost
    template_name = 'blog/DLblogLink.html'
    context_object_name = "all_posts"
    paginate_by = 3
    paginate_orphans = 1

    # handle Http-404 error
    def get_context_data(self, *args, **kwargs):
        try:
            return super(DLBlogListView, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(DLBlogListView, self).get_context_data(*args, **kwargs)


class DLBlogDetailView(DetailView):
    model = DLBlogPost
    template_name = 'blog/MLSinglePost.html'
    context_object_name = "post"


# For the random post
class RandomBlopPostTemplateView(TemplateView):
    template_name = 'blog/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        python_all_posts = PythonBlogPost.objects.all()
        django_all_posts = DjangoBlogPost.objects.all()
        ML_all_posts = MLBlogPost.objects.all()
        DL_all_posts = DLBlogPost.objects.all()

        if len(python_all_posts) and len(django_all_posts) and len(ML_all_posts) and len(DL_all_posts) > 10:
            python_posts = random.sample(
                population=list(python_all_posts), k=8)
            django_posts = random.sample(
                population=list(django_all_posts), k=8)
            ml_posts = random.sample(population=list(ML_all_posts), k=8)
            dl_posts = random.sample(population=list(DL_all_posts), k=8)

        elif len(python_all_posts) and len(django_all_posts) and len(ML_all_posts) and len(DL_all_posts) < 10:
            python_posts = random.sample(
                population=list(python_all_posts), k=4)
            django_posts = random.sample(
                population=list(django_all_posts), k=4)
            ml_posts = random.sample(population=list(ML_all_posts), k=4)
            dl_posts = random.sample(population=list(DL_all_posts), k=4)

        context['python_posts'] = python_posts
        context['django_posts'] = django_posts
        context['ml_posts'] = ml_posts
        context['dl_posts'] = dl_posts

        return context


class AboutTemplateView(TemplateView):
    template_name = 'blog/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_data = AboutUs.objects.all()
        context['all_posts'] = all_data
        return context


# Contact Form
# form object will be automatic pass to the template
class ContactFormView(FormView):
    template_name = 'blog/contact.html'
    form_class = ContactModelForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
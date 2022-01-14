from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from .models import (PythonBlogPost, DjangoBlogPost,
                     MLBlogPost, DLBlogPost, AboutUs, PythonBlogComment,
                     DjangoBlogComment, MLBlogComment, DLBlogComment)
from .forms import ContactModelForm
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
import random
import time
from django.contrib import messages
from django.core.paginator import Paginator
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


# class PythonBlogDetailView(DetailView):
#     model = PythonBlogPost
#     template_name = 'blog/pythonSinglePost.html'
#     context_object_name = "post"

def PythonSingleBlog(request, slug):
    post = PythonBlogPost.objects.get(slug=slug)
    comments = PythonBlogComment.objects.filter(post=post, parent=None)
    replies = PythonBlogComment.objects.filter(post=post).exclude(parent=None)

    replyDict = {}

    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context = {
        'post': post,
        'comments': comments,
        'replyDict': replyDict
    }
    return render(request=request, template_name="blog/pythonSinglePost.html", context=context)


def PythonpostComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = PythonBlogPost.objects.get(id=postSno)
        parentSno = request.POST.get("parentSno")

        if parentSno == "":
            comment = PythonBlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request=request, message="Comment submitted")
        else:
            parent = PythonBlogComment.objects.get(sno=parentSno)
            comment = PythonBlogComment(
                comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request=request, message="Reply submitted")

    return HttpResponseRedirect(redirect_to=f'/pythonSingle_post/{post.slug}')


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


# class DjangoBlogDetailView(DetailView):
#     model = DjangoBlogPost
#     template_name = 'blog/djangoSinglePost.html'
#     context_object_name = "post"

def DjangoSingleBlog(request, slug):
    post = DjangoBlogPost.objects.get(slug=slug)
    comments = DjangoBlogComment.objects.filter(post=post, parent=None)
    replies = DjangoBlogComment.objects.filter(post=post).exclude(parent=None)

    replyDict = {}

    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context = {
        'post': post,
        'comments': comments,
        'replyDict': replyDict
    }
    return render(request=request, template_name="blog/djangoSinglePost.html", context=context)


def DjangopostComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = DjangoBlogPost.objects.get(id=postSno)
        parentSno = request.POST.get("parentSno")

        if parentSno == "":
            comment = DjangoBlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request=request, message="Comment submitted")
        else:
            parent = DjangoBlogComment.objects.get(sno=parentSno)
            comment = DjangoBlogComment(
                comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request=request, message="Reply submitted")

    return HttpResponseRedirect(redirect_to=f'/DjangoSingle_post/{post.slug}')


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


# class MLBlogDetailView(DetailView):
#     model = MLBlogPost
#     template_name = 'blog/MLSinglePost.html'
#     context_object_name = "post"


def MLSingleBlog(request, slug):
    post = MLBlogPost.objects.get(slug=slug)
    comments = MLBlogComment.objects.filter(post=post, parent=None)
    replies = MLBlogComment.objects.filter(post=post).exclude(parent=None)

    replyDict = {}

    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context = {
        'post': post,
        'comments': comments,
        'replyDict': replyDict
    }
    return render(request=request, template_name="blog/MLSinglePost.html", context=context)


def MLpostComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = MLBlogPost.objects.get(id=postSno)
        parentSno = request.POST.get("parentSno")

        if parentSno == "":
            comment = MLBlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request=request, message="Comment submitted")
        else:
            parent = MLBlogComment.objects.get(sno=parentSno)
            comment = MLBlogComment(
                comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request=request, message="Reply submitted")

    return HttpResponseRedirect(redirect_to=f'/MLSingle_post/{post.slug}')


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


# class DLBlogDetailView(DetailView):
#     model = DLBlogPost
#     template_name = 'blog/DLSinglePost.html'
#     context_object_name = "post"


def DLSingleBlog(request, slug):
    post = DLBlogPost.objects.get(slug=slug)
    comments = DLBlogComment.objects.filter(post=post, parent=None)
    replies = DLBlogComment.objects.filter(post=post).exclude(parent=None)

    replyDict = {}

    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context = {
        'post': post,
        'comments': comments,
        'replyDict': replyDict
    }
    return render(request=request, template_name="blog/DLSinglePost.html", context=context)


def DLpostComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = DLBlogPost.objects.get(id=postSno)
        parentSno = request.POST.get("parentSno")

        if parentSno == "":
            comment = DLBlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request=request, message="Comment submitted")
        else:
            parent = DLBlogComment.objects.get(sno=parentSno)
            comment = DLBlogComment(
                comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request=request, message="Reply submitted")

    return HttpResponseRedirect(redirect_to=f'/DLSingle_post/{post.slug}')


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


# comment: User Search Functions
def postSearch(request):
    start_time = time.time()
    querys = request.GET.get('query')

    if len(querys) > 60:
        python_posts = PythonBlogPost.objects.none()
        django_posts = DjangoBlogPost.objects.none()
        ml_posts = MLBlogPost.objects.none()
        dl_posts = DLBlogPost.objects.none()
    else:
        python_posts = PythonBlogPost.objects.filter(title__icontains=querys)
        django_posts = DjangoBlogPost.objects.filter(title__icontains=querys)
        ml_posts = MLBlogPost.objects.filter(title__icontains=querys)
        dl_posts = DLBlogPost.objects.filter(title__icontains=querys)
    

    len_post = [i.count() for i in (python_posts, django_posts, ml_posts,dl_posts) if i.count() > 0]

    if len_post:
        len_post = len_post[0]
    else:
        len_post = 0
    

    all_posts = python_posts.union(django_posts, ml_posts, dl_posts)
    paginator = Paginator(object_list=all_posts, per_page=3, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(number=page_number)


    end_time = time.time()
    total_amountOf_time_taken = end_time - start_time
    total_amountOf_time_taken = round(number=total_amountOf_time_taken, ndigits=5)

    context = {
        'python_posts': python_posts,
        'django_posts': django_posts,
        'ml_posts': ml_posts,
        'dl_posts': dl_posts,
        'total_time_taken': total_amountOf_time_taken,
        'query': querys,
        'len_post' : len_post,
        'page_obj' : page_obj
    }

    return render(request=request, template_name="blog/search.html", context=context)

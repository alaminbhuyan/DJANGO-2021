from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import Http404
from .models import Post


# Create your views here.

# def home(request):
#     all_post = Post.objects.all().order_by('id')
#     # my_paginator = Paginator(object_list=all_post, per_page=3)
#     my_paginator = Paginator(object_list=all_post, per_page=3, orphans=1)
#     page_number = request.GET.get('page')
#     page_obj = my_paginator.get_page(number=page_number)
#     return render(request=request, template_name="blogs/home.html", context={"all_post":page_obj})


class PostListView(ListView):
    model = Post
    template_name = "blogs/home.html"
    ordering = ['id']
    paginate_by = 3
    paginate_orphans = 1

    # handle Http-404 error
    def get_context_data(self, *args, **kwargs):
        try:
            return super(PostListView, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(PostListView, self).get_context_data(*args, **kwargs)

class PostListView2(ListView):
    model = Post
    template_name = "blogs/home2.html"
    ordering = ['id']
    # paginate_by = 3 # if this line is comment then is_paginated will be false that's why all object show in webpage
    paginate_orphans = 1

    # handle Http-404 error
    def get_context_data(self, *args, **kwargs):
        try:
            return super(PostListView2, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(PostListView2, self).get_context_data(*args, **kwargs)

# to make 'read more option'
class PostDetailView(DetailView):
    model = Post
    template_name = 'blogs/post.html'
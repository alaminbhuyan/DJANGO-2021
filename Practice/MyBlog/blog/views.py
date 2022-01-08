from django.shortcuts import render
from .models import Post, Atricals


# Create your views here.
def post(request):
    all_post = Post.objects.all()
    # for post in all_post:
    #     print(post.title)
    #     print(post.text)
    return render(request=request, template_name="blog/post.html", context={'all_post' : all_post})


def articles(request):
    all_articles = Atricals.objects.all()
    return render(request=request, template_name="blog/articles.html", context={'all_articles' : all_articles})
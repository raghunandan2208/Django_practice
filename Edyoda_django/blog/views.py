from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from blog.models import Category
# Create your views here.

def index(request, *args, **kwargs):
    posts = Post.objects.filter(status = "P")
    category = Category.objects.all()
    context = {
    'posts' : posts,
    'category' : category
    }
    return render(request, 'blog/edyoda_stories_main.html', context)

def post_details(request, id, *args, **kwargs):
    try:
        post = Post.objects.get(id = id)
        context = {
        'post' : post
        }
        return render(request, 'blog/details.html', context)
    except:
        return HttpResponse("Invalid ID")

def category_buttons(request, id, *args, **kwargs):
    posts = Post.objects.filter(category__id = id)
    context = {
    'posts' : posts
    }
    return render(request, 'blog/edyoda_stories_main.html', context)

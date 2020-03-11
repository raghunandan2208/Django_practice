from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.

def index(request, *args, **kwargs):
    posts = Post.objects.filter(status = "P")


    context = {
    'posts' : posts
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

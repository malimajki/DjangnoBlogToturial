from django.shortcuts import render
from .models import Category, Post

def home_view(request):
    posts = Post.objects.all()
    context = {
        "posts":posts
    }
    return render (request, "blog/home.html", context)
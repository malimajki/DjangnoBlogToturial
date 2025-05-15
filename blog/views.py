from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Post
from .forms import PostForm, CategoryForm

def home_view(request):
    posts = Post.objects.all()
    categories = Category.objects.all()

    active_category = request.GET.get('category', '')

    if active_category:
        posts = posts.filter(category__slug=active_category)

    context = {
        "posts":posts,
        "categories":categories,
        "active_category":active_category
    }
    return render (request, "blog/home.html", context)

def post_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect (home_view)
    else: 
        form = PostForm()
    return render (request, "blog/post_form.html", {"form":form})

def post_update_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

def post_delete_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        post.delete()
        return redirect('home')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

def category_create_view(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect (home_view)
    else:
        form = CategoryForm()
    return render (request, "blog/category_form.html", {"form":form})

def category_update_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=category.slug)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'blog/post_form.html', {'form': form})

def category_delete_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == "POST":
        category.delete()
        return redirect('home')
    return render(request, 'blog/post_confirm_delete.html', {'post': category})
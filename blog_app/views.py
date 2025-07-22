from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
from .models import Blog

@login_required
def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('blog_app:view_blog', blog_id=blog_post.pk)
        else:
            return  HttpResponse("<h1>Failed to add!</h1>")
    form = BlogForm()
    return render(request, 'create_post.html', {'form':form})


def edit_blog(request, blog_id):
    # Get relevant blog post
    # Check if blog post is owned by logged in user
    # Create form with blog post content
    # Send form to template to render.
    try:
        blog_post = Blog.objects.get(pk=blog_id)
        if blog_post.author == request.user:
            form = BlogForm(instance=blog_post)
            return render(request, 'create_post.html', {'form':form})
    except Exception:
        return redirect("blog_app:home")
    


def view_blog(request, blog_id):
    try:
        blog_post = Blog.objects.get(pk=blog_id)
        context = {
            'title' : blog_post.title,
            'body' : blog_post.body,
            'author': blog_post.author.username,
            'blog_id': blog_id
        }
        return render(request, 'view_post.html', context=context)
    except Exception as e:
        print(e)
        return redirect("blog_app:home")

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})
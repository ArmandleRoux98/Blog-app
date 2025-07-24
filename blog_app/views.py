from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
from .models import Blog

@login_required
def create_blog(request):
    """
    GET - Return page with form to create Blog post.
    POST - Create Blog post and redirect to view blog page.
    """
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
    """
    GET- Returns page with form to edit Blog post with given id or redirects 
    to home if Blog post is not found on.
    POST - Edits post with valid form then redirect to view blog on success
    of redirect back to edit page on fail.
    """
    try:
        blog_post = Blog.objects.get(pk=blog_id)
        if blog_post.author == request.user:
            if request.method == "GET":
                form = BlogForm(instance=blog_post)
                return render(request, 'create_post.html', {'form':form})
            elif request.method == "POST":
                form = BlogForm(request.POST, instance=blog_post)
                if form.is_valid():
                    form.save()
                    return redirect("blog_app:view_blog", blog_id=blog_id)
                return redirect("blog_app:edit_blog", blog_id=blog_id)

    except Exception as e:
        print(e)
        return redirect("blog_app:home")
    


def view_blog(request, blog_id):
    """
    Returns page displaying Blog post with given id or redirects 
    home if post is not found.
    """
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
    """Returns page displaying all blog posts available."""
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})
from django.shortcuts import render, redirect

from .models import Blog, BlogPost
from .forms import BlogForm, BlogPostForm

def index(request):
    """The homepage for blogs"""
    return render(request, 'blogs/index.html')

def blogs(request):
    """Show all topics."""
    blogs = Blog.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    """Show a single topic and all its entries."""
    blog = Blog.objects.get(id=blog_id)
    blog_posts = blog.blogpost_set.order_by('-date_added')
    context = {'blog': blog, 'blog_posts': blog_posts}
    return render(request, 'blogs/blog.html', context)

def new_blog(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogForm()
    else:
        # POST data submitted; process data.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')
        
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

def new_blog_post(request, blog_id):
    """Add a new entry for a particular topic."""
    blog = Blog.objects.get(id=blog_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_blog_post = form.save(commit=False)
            new_blog_post.blog = topic
            new_blog_post.save()
            return redirect('blogs:blogs', blog_id=blog_id)

    # Display a blank or invalid form.
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/new_blog_post.html', context)

def edit_blog_post(request, blog_post_id):
    """Edit an existing entry."""
    blog_post = BlogPost.objects.get(id=blog_post_id)
    blog = blog_post.blog

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = BlogPostForm(instance=blog_post)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=blog_post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_post_id=blog_post_id)
        
    context = {'blog_post': blog_post, 'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blog_post.html', context)
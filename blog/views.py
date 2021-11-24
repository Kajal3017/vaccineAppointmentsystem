from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import BlogForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from blog.models import Blog

# show all blogs
def blog_index(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_index.html', {'blogs': blogs})

# show single blog
def blog_detail(request, blog_slug, blog_id):
    blog = get_object_or_404(Blog, slug=blog_slug, pk=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

# create blog
def create_blog(request):
    form = BlogForm()
    if request.method == 'POST' or None:
        form = BlogForm(request.POST)
        if form.is_valid():
            c_form = form.save(commit=False)
            c_form.user = request.user
            c_form.save()
            return redirect(reverse('blog_detail', args=[c_form.slug, c_form.id]))

    dictionary = {'form': form}
    return render(request, 'blog/create_blog.html', dictionary)


#edit blog
def edit_blog(request, blog_slug, blog_id):
    blog = get_object_or_404(Blog, slug=blog_slug, pk=blog_id)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid:
            c_form = form.save(commit=False)
            c_form.user = request.user
            c_form.save()
            messages.info(request, 'Notes detail updated.')
            return redirect(reverse('blog_detail', args=[blog_slug, blog_id]))

    dictionary = {'form': form}
    return render(request, 'blog/edit_blog.html', dictionary) 



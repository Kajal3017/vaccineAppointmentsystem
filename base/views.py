from django.http import HttpResponse
from django.shortcuts import render

from base.forms import BlogForm, ContactForm
from base.models import Blog


def index(request):
    posts = Blog.objects.all()[:10]
    return render(request, 'base/index.html', {'posts': posts})


def projects(request):
    return render(request, 'base/project.html', {})


def all_posts(request):
    all_posts = Blog.objects.all()
    return render(request, 'base/posts.html', {'posts': all_posts})


def skills(request):
    return render(request, 'base/skills.html', {})


def create_blog(request):
    form = BlogForm()
    if request.method == 'POST' or None:
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Notes detail created.')
            return HttpResponse("success")
            # return redirect(reverse('notes:detail', args=[form.slug, form.id]))

    dictionary = {'form': form}
    return render(request, 'base/create_blog.html', dictionary)


def create_contact_us(request):
    form = ContactForm()
    if request.method == 'POST' or None:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Notes detail created.')
            return HttpResponse("success")
            # return redirect(reverse('notes:detail', args=[form.slug, form.id]))

    dictionary = {'form': form}
    return render(request, 'base/create_contact_us.html', dictionary)


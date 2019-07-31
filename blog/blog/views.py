from django.shortcuts import render, get_object_or_404, redirect

from .models import Blog

from django.utils import timezone

# Create your views here.
def index(request):
    blogs = Blog.objects
    return render(request, 'index.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def lists(request):
    blogs = Blog.objects
    return render(request, 'lists.html', {'blogs': blogs})

def about(request):
    return render(request, 'about.html')

def credit(request):
    return render(request, 'credit.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/' + str(blog.id))
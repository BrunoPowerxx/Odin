from django.shortcuts import render
from .models import BlogPost

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'pages/blog.html', {'posts': posts})

def contact(request):
    return render(request, 'pages/contact.html')

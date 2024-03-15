from django.shortcuts import render
from django.db import models
from . import models

# index

def index(request):
    baner = models.Banner.objects.last()
    about_us = models.AboutUs.objects.last()
    services = models.Service.objects.all()
    blogs = models.Blog.objects.all()


    context = {
        'baner':baner,
        'about_us':about_us,
        'services':services,
        'blogs':blogs,
    }
    return render(request, 'index.html', context)

# about us

def aboutus(request):
    about_us = models.AboutUs.objects.last()
    context = {
        'about_us':about_us
    }
    return render(request, 'about.html', context)

# contact

def contact(request):
    if request.method == 'POST':
        try:
            models.Contact.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                phone=request.POST['phone'],
                body=request.POST['message']
            )
        except:
            ...
    return render(request, 'contact.html')

# service

def service(request):
    services = models.Service.objects.all()
    context = {
        'services':services
    }
    return render(request, 'service.html', context)

# Blog 


def blog(request):
    blogs = models.Blog.objects.all()
    
    context = {
        'blogs':blogs
    }

    return render(request, 'blog.html', context)
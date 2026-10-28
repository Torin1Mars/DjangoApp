from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


# Create your views here.


def home_page(request):
    return render(request, 'projectApp/home.html')

def about(request):
    return render(request, 'projectApp/about.html')

def post_list(request):
    postsData = Post.objects.all().order_by('date')
    return render(request, 'projectApp/post_list.html', {'posts':postsData})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'projectApp/post_page.html', {'post': post})
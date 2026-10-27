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
    return render(request, 'projectApp/post.html', {'posts':postsData})
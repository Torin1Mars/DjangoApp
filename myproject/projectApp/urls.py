from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name = "home"),
    path('about/', views.about, name = "about"),
    path('post/', views.post_list, name = "post_list")
]
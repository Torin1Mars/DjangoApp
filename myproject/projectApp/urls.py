from django.conf.urls.static import static
from django.urls import path
from . import views
from myproject import settings

app_name = 'posts'

urlpatterns = [
    path('', views.home_page, name = "home"),
    path('about/', views.about, name = "about"),
    path('post_list/', views.post_list, name = "post_list"),
    path('<slug:slug>', views.post_page, name="page")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

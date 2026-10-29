from django.conf.urls.static import static
from django.urls import path
from . import views
from myproject import settings

app_name = 'users'

urlpatterns = [
    path('registration/', views.register_view, name = "registration"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
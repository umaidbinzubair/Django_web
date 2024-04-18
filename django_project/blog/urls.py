from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from .import views

urlpatterns = [
    path('', views.home,name = 'blog-home'),
    path('about/', views.about, name='blog-about')
]

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blogpost/<str:slug>', views.blogpost, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
]

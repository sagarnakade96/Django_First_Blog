from blog.models import Blog
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def blog(request):
     blogs = Blog.objects.all
     context  = {'blogs':blogs}
     return render(request,'bloghome.html',context)

def blogpost(request,slug):
     blogs = Blog.objects.filter(slug = slug).first()
     context = {'blogs': blogs}

     return render(request,'blogpost.html',context)

def contact(request):
     return render(request,'contact.html')

def search(request):
     return render(request,'search.html')
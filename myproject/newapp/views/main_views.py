from django.shortcuts import render
from myapp.models import Blog

def index(request):
    blog=Blog.objects.all()
    return render(request,'main/indexo.html',{'blog':blog})
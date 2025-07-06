from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def addblog(request):
    return render(request, 'main/addblog.html')


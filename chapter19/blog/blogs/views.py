from django.shortcuts import render

def index(request):
    """The homepage for blogs"""
    return render(request, 'blogs/index.html')
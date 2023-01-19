from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def list_blogs(request):
    blogs = Blog.objects.all()
    context = {"blogs":blogs}
    return render(request, "blog/list.html", context)


def detail_blog(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    context = {'blog':blog}
    return render(request, "blog/detail.html", context)

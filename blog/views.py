from django.shortcuts import render
from django.http import HttpResponse
from . models import Post
# Create your views here.
def blogHome(request):
    allpost = Post.objects.all()
    contex = {
        'allpost':allpost,
    }
    return render(request,'blog/bloghome.html',contex)

def blogPost(request ,slug):
    post = Post.objects.filter(slug=slug)[0]
    contex = {
        'post':post,
    }
    return render(request,'blog/blogpost.html',contex)

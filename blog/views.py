from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def blogHome(request):
    return HttpResponse('This is blog home... we will keep all our blog posts')

def blogPost(request ,slug):
    return HttpResponse(f'This is blogpost : {slug}')

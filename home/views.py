from django.shortcuts import render
from django.http import HttpResponse
from . models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):    
    if request.method=='POST':
        s_name=request.POST['name']
        s_email=request.POST['email']
        s_phone=request.POST['phone']
        s_content=request.POST['content']
        if len(s_name)<2 or len(s_email)<3 or len(s_phone)<10 or len(s_content)<5:
            messages.warning(request, 'please fill the form correctly')
        else:
            contact = Contact(email=s_email,phone=s_phone,content=s_content,name=s_name)
            contact.save()
            messages.success(request, 'Welcome to contact.')
    return render(request,'home/contact.html')
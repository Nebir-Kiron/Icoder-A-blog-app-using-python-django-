from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from blog.models import Post

# Create your views here.
# HTML pages
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

def search(request):
    query = request.GET['search']

    if len(query) > 80 or len(query) < 3:
        allpost = Post.objects.none()
    else:    
        allposttitle = Post.objects.filter(title__icontains=query)
        allpostcontent = Post.objects.filter(content__icontains=query)
        allpost = allposttitle.union(allpostcontent)

    if allpost.count() == 0:
        messages.warning(request, 'No search results found..please refine your query')
        
    contex = {
        'allpost':allpost,
        'query':query,
    }
    return render(request,'home/search.html',contex)


# Authentication API's
def handlesignup(request):
    if request.method == "POST":
        # get the post values
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        

        # check all the requiements
        if len(username) > 10:
            messages.error(request,'username must be under 10 character')
            return redirect('/')

        if not username.isalnum():
            messages.error(request,'username should contains only character and number')
            return redirect('/')            

        if pass1 != pass2:
            messages.error(request,'password doesn\'t match')
            return redirect('/')



        # create user
        user = User.objects.create_user(username , pass1 , email)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(request,'You have created account successfully') 
        return redirect('/')
    
    else:
        return HttpResponse('404 -- Not found')

def handlelogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
    
        user = authenticate(username = loginusername, password = loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,'successfully loged in')
            return redirect('/')
        else:
            messages.error(request,'username or password doese not match')
            return redirect('/')

    return HttpResponse('404 -- Not found')

def handlelogout(request):
    
    logout(request)
    messages.success(request,'successfully loged out')
    return redirect('/')


    
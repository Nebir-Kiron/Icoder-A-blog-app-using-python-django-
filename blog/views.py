from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from . models import Post,BlogComment
from blog.templatetags import extras
# Create your views here.
def blogHome(request):
    allpost = Post.objects.all()
    contex = {
        'allpost':allpost,
    }
    return render(request,'blog/bloghome.html',contex)

def blogPost(request ,slug):
    post = Post.objects.filter(slug=slug)[0]
    comments = BlogComment.objects.filter(post=post,parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replydict = {}
    for reply in replies:
        if reply.parent.si_no not in replydict:
            replydict[reply.parent.si_no] = [reply]
        else:
            replydict[reply.parent.si_no].append(reply)
    print(replydict)
    contex = {
        'post':post,
        'comments':comments,
        'user': request.user,
        'replydict':replydict,
    }
    return render(request,'blog/blogpost.html',contex)

def postComment(request):
    if request.method=="POST":
        cmnt = request.POST.get("comment")
        user = request.user
        postsno = request.POST.get("postsno")
        post = Post.objects.get(serial_no=postsno)
        parentsino = request.POST.get("sino")

        if parentsino == "":
            comment = BlogComment(comment=cmnt,user=user,post=post)
            comment.save()
            messages.success(request, 'Your comment has posted successfully')
        else:
            parent = BlogComment.objects.get(si_no=parentsino)
            comment = BlogComment(comment=cmnt,user=user,post=post,parent=parent)
            comment.save()
            messages.success(request, 'Your reply has posted successfully')

    return redirect(f'/blog/{post.slug}')
    
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # API to post a comment
    path('postcomment/', views.postComment,name='postcomment'),


    path('',views.blogHome,name='blogHome'),
    path('<str:slug>',views.blogPost,name='blogPost'),
]
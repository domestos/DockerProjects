"""   URLS BLOG """
from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    #path('post/<str:slug>/', post_detail, name='post_detail_url'),
    path('post/<str:slug>/', PostDetail.as_view() , name='post_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    #path('tag/<str:slug>/', tag_detail, name='tag_detail_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
]

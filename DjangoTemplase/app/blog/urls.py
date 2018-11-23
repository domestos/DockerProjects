"""   URLS BLOG """
from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *

# це список і порядок правил має значення
# This is a list and the order of the rules matters
urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('tags/', tags_list, name='tags_list_url'),
    #POST
    path('post/create/', PostCreate.as_view() , name='post_create_url'),
    #path('post/<str:slug>/', post_detail, name='post_detail_url'),
    path('post/<str:slug>/', PostDetail.as_view() , name='post_detail_url'),
    path('post/<str:slug>/update', PostUpdate.as_view(), name='post_update_url'),
    #TAG
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    #path('tag/<str:slug>/', tag_detail, name='tag_detail_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update', TagUpdate.as_view(), name='tag_update_url'),


]

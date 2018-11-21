from django.shortcuts import render
from django.views.generic import View
from .models import *
# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request,'blog/index.html', context={'posts':posts})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags':tags} )



def tag_detail(request, slug):
    tag  = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', context={'tag':tag})


###=============================================================================
#USE Method
#def post_detail(request, slug):
#    post = Post.objects.get(slug__iexact=slug)
#    return render(request, 'blog/post_detail.html', context={'post':post})

#USE CLASS
#create the class PostDetail and this class extends from View
# we get all values and methods from View
class PostDetail(View):
    def get(self, request, slug)
        post = Post.objects.get(slug__iexact=slug)
        return render(request, 'blog/post_detail.html', context={'post':post})

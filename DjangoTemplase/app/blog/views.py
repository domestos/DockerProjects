from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .models import *
from .utils import OjbectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin
from .forms import TagForm, PostForm
# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request,'blog/index.html', context={'posts':posts})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags':tags} )

###======================= The POST ============================================
#USE Method
#def post_detail(request, slug):
#    post = Post.objects.get(slug__iexact=slug)
#    return render(request, 'blog/post_detail.html', context={'post':post})

#USE CLASS WHIT MIXIN
#create the class PostDetail and this class extends from View
# we get all values and methods from View
#class PostDetail(View):
#    def get(self, request, slug):
#        #post = Post.objects.get(slug__iexact=slug)
#        post = get_object_or_404(Post,slug__iexact=slug)
#        return render(request, 'blog/post_detail.html', context={'post':post})

#USE CLASS WHIT MIXIN
class PostDetail(OjbectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'
#  Post.mro() - показує порядок пошуку атребутів класу


class PostCreate(ObjectCreateMixin, View):
    model_form =PostForm
    template =  'blog/post_create_form.html'

class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = "blog/post_update_form.html"

#    def get(self, request):
#    def get(self, request):
#         form = PostForm()
#         return render(request, 'blog/post_create_form.html', context={'form':form})

#    def post(self, request):
#        bound_form = PostForm(request.POST)
#        if bound_form.is_valid():
#            new_post = bound_form.save()
#            return redirect(new_post)
#        return render(request, 'blog/post_create_form.html', context={'form': bound_form} )

###======================= The TAG  ============================================
#USE Method
#def tag_detail(request, slug):
#    tag  = Tag.objects.get(slug__iexact=slug)
#    return render(request, 'blog/tag_detail.html', context={'tag':tag})

#USE CLASS
#class TagDetail(View):
#    def get(self, request, slug):
#        tag = get_object_or_404(Tag, slug__iexact=slug)
#        return render(request, 'blog/tag_detail.html', context={'tag':tag})

#USE CLASS WHIT MIXIN
class TagDetail(OjbectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    model_form =TagForm
    template = 'blog/tag_create.html'
#    def get(self, request):
#        form = TagForm()
#        return render(request, "blog/tag_create.html", context={'form':form})

#    def post(self,request):
#        bound_form =TagForm(request.POST)
#        if bound_form.is_valid():
#            new_tag = bound_form.save()
#            return redirect(new_tag)
#        return render(request, 'blog/tag_create.html',context={'form':bound_form })
class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = "blog/tag_update_form.html"

#    def get(self, request, slug):
#        tag = Tag.objects.get(slug__iexact=slug)
#        bound_form = TagForm(instance=tag)
#        return render(request, "blog/tag_update_form.html", context={'form':bound_form, 'tag': tag})

#    def post(self, request, slug):
#        tag = Tag.objects.get(slug__iexact=slug)
#        bound_form = TagForm(request.POST, instance=tag)
#        if bound_form.is_valid():
#            new_tag = bound_form.save()
#            return redirect(new_tag)
#        return render(request, "blog/tag_update_form.html",  context={'form':bound_form, 'tag': tag})

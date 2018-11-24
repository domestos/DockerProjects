from django.shortcuts import redirect

#redirect has two kinds.
# 1) static = 301 if need activate --> permanent=True
# 2) dynamic = 302 is default
def redirect_blog(request):
    return redirect('posts_list_url', permanent=True)

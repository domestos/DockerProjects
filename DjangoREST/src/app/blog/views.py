from django.shortcuts import render

# Create your views here.
#========== OLD
#from django.http import  HttpResponse
#def post_list(request):
#    return HttpResponse("<h1>valera</h1>")

from django.http import  HttpResponse
def post_list(request):
    return render(request, 'blog/index.html' )

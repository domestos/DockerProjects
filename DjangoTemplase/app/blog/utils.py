from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *

class OjbectDetailMixin:
    model = None
    template =None

    def get(self, request, slug):
        #post = Post.objects.get(slug__iexact=slug)
        obj = get_object_or_404( self.model,slug__iexact=slug)
        #self.model.__name__.lower() - get name of models (Post or Tag) and set lower
        return render(request, self.template   , context={self.model.__name__.lower():obj})

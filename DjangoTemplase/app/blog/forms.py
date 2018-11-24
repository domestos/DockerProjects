from django import forms
from django.core.exceptions import ValidationError
from .models import Tag, Post

#ModelForm Has the special method save
class TagForm(forms.ModelForm):

    #class TagForm(forms.Form):
    #title = forms.CharField(max_length=50)
    #slug = forms.CharField(max_length=50)
    #title.widget.attrs.update({'class':'form-control'})
    #slug.widget.attrs.update({'class':'form-control'})
    class Meta:
        model = Tag
        fields = ['title','slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug mast be unique. this slug "{}" is already'.format(new_slug))
        return new_slug


    #override method save() in calss forms
    #def save(self):
    #    #cread a new Objcet Tag and save to databes
    #    new_tag = Tag.objects.create(
    #        title =self.cleaned_data['title'],
    #        slug=self.cleaned_data['slug']
    #    )
    #    #return saved object tag
    #    return new_tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','slug','body','tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        return new_slug

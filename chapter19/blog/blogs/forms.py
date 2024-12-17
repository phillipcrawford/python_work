from django import forms

from .models import Blog, BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name']
        labels = {'name': ''}

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body']
        labels = {'title': '', 'body': ''}        
        widgets = {'title': forms.Textarea(attrs={'cols': 80}), 
                   'body': forms.Textarea(attrs={'cols': 80})}
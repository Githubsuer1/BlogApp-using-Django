from django.forms import ModelForm
from .models import Blog
from django import forms

class createBlogForm(ModelForm):
    title = forms.CharField(widget=forms.Textarea(attrs={
        'class':'w-full max-w-md rounded',
        'type':'text',
        'placeholder':'Enter title'
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class':'mt-5',
        'type':'file',
    }))
    class Meta:
        model = Blog
        fields = ['title','image']

class editBlogForm(ModelForm):
    title = forms.CharField(widget=forms.Textarea(attrs={
        'class':'w-full max-w-md rounded',
        'type':'text',
        'placeholder':'Enter title'
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class':'mt-5',
        'type':'file',
    }))
    class Meta:
        model = Blog
        fields = ['title','image']

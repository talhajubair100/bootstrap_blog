from django import forms
from .models import Category, Post

class CreateCategory(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'file-input'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),


        }


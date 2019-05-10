from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': '제목.'}),
            
        }
        
        labels = {
            'title' : '제목',
            'body' : '내용',        
            }
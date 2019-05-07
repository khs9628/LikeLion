from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['donkey_title', 'donkey_name','donkey_content','donkey_hits']
from django import forms
from .models import Blog, Comment

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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_text"]
        widgets = {
            'comment_text': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': '댓글 등록'}),
            
        }
        
        labels = {
            'comment_text' : '댓글',       
            }

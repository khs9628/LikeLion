from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .forms import BlogForm, CommentForm
from .models import Blog, Comment


# index페이지
def layout(request):
        return render(request, 'crud/layout.html')

# 전체글 보여주는 페이지
def home(request):
        blogs = Blog.objects
        return render(request, 'crud/home.html', {'blogs': blogs})

# 새글 등록
def new(request):
        return render(request, 'crud/new.html')

def create(request):
        blog = Blog()
        blog.title = request.GET['title']
        blog.body = request.GET['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/crud/home/')

def blogform(request, blog=None):
        if request.method == 'POST':
                form = BlogForm(request.POST, instance=blog)
                if form.is_valid():
                        blog = form.save(commit=False)
                        blog.pub_date = timezone.now()
                        blog.save()    
                        return redirect('crud:home')
        else:
                form = BlogForm(instance=blog)
                return render(request, 'crud/new.html', {'form':form})      

# 글수정
def edit(request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        return blogform(request, blog)

# 글삭제
def remove(request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()
        return redirect('crud:home')

# 글 댓글 상세보기 기능
def detail(request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        if request.method == "POST":
                form = CommentForm(request.POST)
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.Blog_pk = blog
                        comment.comment_text = form.cleaned_data["comment_text"]
                        comment.save()
                        return redirect("crud:detail", blog.pk)
        else:
                form = CommentForm()
                return render(request, "crud/detail.html", {"blog" : blog, "form" : form})


#댓글 수정
def comment_update(request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        blog = comment.Blog_pk
        if request.method == "POST":
                form = CommentForm(request.POST, instance=comment)
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.Blog_pk = blog
                        comment.comment_text = form.cleaned_data["comment_text"]
                        comment.save()
                        return redirect("crud:detail", blog.pk)
        else:
                form = CommentForm(instance=comment)
                return render(request, "crud/newComment.html", {'form' : form,})

#댓글 삭제
def comment_delete(request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        blog = comment.Blog_pk
        comment.delete()
        return redirect("crud:detail", blog.pk)



# 부가기능 
def login(request):
        return render(request, 'crud/login.html')

def register(request):
        return render(request, 'crud/register.html')

def tables(request):
        return render(request, 'crud/tables.html')
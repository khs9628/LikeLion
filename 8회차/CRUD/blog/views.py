from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .forms import BlogForm
from .models import Blog


from .models import Blog
# Create your views here.

def layout(request):
    return render(request, 'blog/layout.html')

def home(request):
    blogs = Blog.objects
    return render(request, 'blog/home.html', {'blogs': blogs})

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    blog = Blog()
    blog.donkey_title = request.GET['donkey_title']
    blog.donkey_content = request.GET['donkey_content']
    blog.donkey_name  = request.GET['donkey_name']
    blog.donkey_time = timezone.datetime.now()
    blog.donkey_hits = request.GET['donkey_hits']
    blog.save()
    return redirect('/blog/home/')

def blogform(request, blog=None):
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.donkey_time = timezone.now()
            blog.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)
        return render(request, 'blog/new.html', {'form':form})      

def edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return blogform(request, blog)

def remove(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('home')
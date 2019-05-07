from django.shortcuts import render

# Create your views here.

def layout(request):
    return render(request,'app/layout.html')

def home(request):
    return render(request,'app/home.html')    

def form(request):
    full_text=request.GET['fulltext']
    return render(request, 'app/form.html' , {'fulltext':full_text})    

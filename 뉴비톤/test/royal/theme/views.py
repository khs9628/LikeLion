from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "theme/index.html")

def login(request):
    return render(request, "theme/login.html")

def signin(request):
    return render(request, "theme/signin.html")

def about(request):
    return render(request, "theme/about.html")
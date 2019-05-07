from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Donkey, Health, Aicohol
# Create your views here.

# Create your views here.
def index(request):
    return render(request, "board/index.html")

def login(request):
    return render(request, "board/login.html")

def signin(request):
    return render(request, "board/signin.html")

def about(request):
    return render(request, "board/about.html")

def mypage(request):
    return render(request, "board/mypage.html")

def medicine(request):
    return render(request, "board/medicine.html")

def recipe(request):
    return render(request, "board/recipe.html")
                  
# 창 띄우기
def home(request):
    donkeys = Donkey.objects
    return render(request,'home.html',{'donkeys':donkeys})

def health(request):
    healths = Health.objects
    return render(request,'health.html',{'healths':healths})

def aicohol(request):
    aicohols = Aicohol.objects
    return render(request,'aicohol.html',{'aicohols':aicohols})

# 디테일창 만들기
def detail_home(request,donkey_id):
    donkeyss = get_object_or_404(Donkey, pk=donkey_id)
    return render(request, 'detail_home.html',{'donkey':donkeyss})

def detail_health(request,health_id):
    healthss = get_object_or_404(Health, pk=health_id)
    return render(request, 'detail_health.html',{'health':healthss})

def detail_aicohol(request,aicohol_id):
    aicoholss = get_object_or_404(Aicohol, pk=aicohol_id)
    return render(request, 'detail_aicohol.html',{'aicohol':aicoholss})

# 새 테이블 만들기

def new_home(request):
    return render(request, 'new_home.html')
    
def new_health(request):
    return render(request, 'new_health.html')

def new_aicohol(request):
    return render(request, 'new_aicohol.html')

# 새창 만들기

def create_home(request):
    donkey = Donkey()
    donkey.title = request.GET['title']
    donkey.body = request.GET['body']
    donkey.pub_date = timezone.datetime.now()
    donkey.name = request.GET['name']
    donkey.save()

    return redirect("board:detail_home", donkey.id)

def create_health(request):
    health = Health()
    health.title = request.GET['title']
    health.body = request.GET['body']
    health.pub_date = timezone.datetime.now()
    health.name = request.GET['name']
    health.save()
    
    return redirect("board:detail_health", health.id)

def create_aicohol(request):
    aicohol = Aicohol()
    aicohol.title = request.GET['title']
    aicohol.body = request.GET['body']
    aicohol.pub_date = timezone.datetime.now()
    aicohol.name = request.GET['name']
    aicohol.save()

    return redirect("board:detail_aicohol", aicohol.id)
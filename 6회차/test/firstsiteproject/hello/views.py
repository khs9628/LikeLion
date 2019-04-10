from django.shortcuts import render

 # 요청이 들어오면 home.html파일을 열어주는 home이라는 함수# Create your views here.
def home(request):
    return render(request, 'hello/home.html')

   
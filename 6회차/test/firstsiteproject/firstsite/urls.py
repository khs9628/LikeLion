"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import hello.views #view.py를 읽어와야하니 import해준다

urlpatterns = [
     # path를 추가해준다
    path('admin/', admin.site.urls),
   
    # 도메인 뒤에 붙는 url , views안에 저의된 함수 , path의 name을 home이라고 지정
    path('', hello.views.home, name='home'),
]

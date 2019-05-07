
from django.contrib import admin
from django.urls import path
# app에 views.py를 import한다
import crud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crud.views.layout, name='layout'),
    path('crud/home/', crud.views.home, name='home'),
    path('crud/new/', crud.views.new, name = 'new'),
    path('crud/create/', crud.views.create, name = 'create'),
    path('crud/newblog/', crud.views.blogform, name = 'newblog'),
    path('crud/<int:pk>/edit/', crud.views.edit, name = 'edit'),
    path('crud/<int:pk>/remove/', crud.views.remove, name = 'remove'),
    path('crud/login/', crud.views.login, name = 'login'),
    path('crud/register/', crud.views.register, name = 'register'),
    path('crud/tables/', crud.views.tables, name = 'tables'),
]

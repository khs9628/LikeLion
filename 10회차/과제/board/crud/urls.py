from django.urls import path
from . import views

app_name = "crud"

urlpatterns = [
    path("", views.layout, name='layout'),
    path('home/', views.home, name='home'),
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'),
    path('newblog/', views.blogform, name = 'newblog'),
    path('edit/<int:pk>/', views.edit, name = 'edit'),
    path('remove/<int:pk>/', views.remove, name = 'remove'),
    
    path('home/<int:pk>/', views.detail, name = 'detail'),
    path('comment_update/<int:pk>/', views.comment_update, name = 'comment_update'),
    path('comment_delete/<int:pk>/', views.comment_delete, name = 'comment_delete'),

# extra 페이지
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('tables/', views.tables, name = 'tables'),
]


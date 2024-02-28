from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_register),
    path('login/', views.user_login),
    path('users/new', views.user_register),
    path('users', views.users_list),
    path('', views.blog_redirect)
]

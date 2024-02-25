from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('redirect_path', views.redirect_view),
    path('redirected_path', views.redirected_view),
]
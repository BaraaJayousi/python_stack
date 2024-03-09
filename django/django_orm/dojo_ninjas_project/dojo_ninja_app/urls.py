from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('add-ninja/', views.add_ninja),
    path('add-dojo/', views.add_dojo)
]

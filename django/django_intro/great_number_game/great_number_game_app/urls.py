from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('reset-game', views.reset_game),
    path('check-answer', views.check_answer)
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="my_counter"),
    path('counter-actions',views.counter_actions)
]

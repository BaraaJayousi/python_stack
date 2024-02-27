from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="my_counter"),
    path('destroy_session',views.destroy_session)
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.render_form, name='render-form'),
    path('register-user', views.register_user, name='register_user'),
    path('login-user',views.login_user, name='login_user'),
    path('success', views.render_success, name='render_success'),
    path('logout-user', views.logout_user, name='logout_user')
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.render_main_page, name='render_main_page'),
    path('post-user-message', views.post_user_message, name="post_user_message"),
    path('post-user-comment', views.post_user_comment, name='post_user_comment'),
    path('process-message',views.process_message, name='process_message')
]

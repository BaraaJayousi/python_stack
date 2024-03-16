from django.urls import path
from . import views


urlpatterns = [
    path('',views.render_courses, name='render_courses'),
    path('add-course', views.add_course, name='add_course'),
    path('courses/destroy/<int:course_id>',views.destroy_course, name='destroy_course')
]

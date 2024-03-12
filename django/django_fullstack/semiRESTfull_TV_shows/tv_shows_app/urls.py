from django.urls import path
from . import views
urlpatterns = [
    path('',views.render_shows, name="render_shows"),
    path('/new',views.render_new_show_form, name="render_new_show_form"),
    path('/new/add-new-show', views.add_new_show, name='add_new_show'),
    path('/<int:show_id>',views.show_details, name="render_show_details"),
    path('/<int:show_id>/edit', views.edit_show, name='edit_show')
]

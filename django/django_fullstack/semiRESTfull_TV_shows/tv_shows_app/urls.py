from django.urls import path
from . import views
urlpatterns = [
    path('',views.redirect_to_shows),
    path('shows',views.render_shows, name="render_shows"),
    path('shows/new',views.render_new_show_form, name="render_new_show_form"),
    path('shows/new/add-new-show', views.add_new_show, name='add_new_show'),
    path('shows/<int:show_id>',views.show_details, name="render_show_details"),
    path('shows/<int:show_id>/edit', views.edit_show, name='edit_show'),
    path('shows/<int:show_id>/update', views.update_show, name='update_show'),
    path('shows/<int:show_id>/destroy', views.delete_show, name="delete_show")
]

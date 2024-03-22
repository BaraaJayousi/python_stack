from django.urls import path
from . import views

urlpatterns = [
    path('',views.render_books_page, name='render_books_page'),
    path('/<int:book_id>', views.show_book, name='show_book'),
    path('add-fav-book', views.add_fav_book, name='add_fav_book'),
    path('edit-book', views.edit_book, name='edit_book'),
    path('process-fav-books', views.process_fav_book, name='process_fav_book')
]
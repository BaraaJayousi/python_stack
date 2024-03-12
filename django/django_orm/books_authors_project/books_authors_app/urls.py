from django.urls import path
from .  import views
urlpatterns = [
    path('',views.books),
    path('add-book', views.add_books),
    path('books/<int:book_id>', views.show_book),
    path('books/<int:book_id>/add-book-author', views.add_book_author),
    path('authors',views.authors),
    path('authors/add-author',views.add_author),
    path('authors/<int:author_id>',views.show_author),
    path('authors/<int:author_id>/add-author-book',views.add_author_book)
]

from django.db import models
from authentication_app.models import Users

# Create your models here.

class BookManager(models.Manager):
    def validate_book(self,book_data):
        errors = {}
        if len(book_data['book_title']) < 2:
            errors['book_title'] = "Book title is required and must be greater than 1 character"
        if len(book_data['book_desc']) < 5:
            errors['book_desc'] = "Book description should at least be 5 characters"

        return errors
    
    def add_book(self, title, description, uploader_id): #returns new book instance
        uploader = Users.objects.get(id = uploader_id)
        new_book = self.create(title=title, description = description, uploaded_by = uploader)
        new_book.user_who_like.add(uploader)
        return new_book
    
    def is_uploader(self, user_id, book_id): #==> returns bool if the book exists and checks if the currernt user is the uploader/owner
        book = self.filter(id = book_id).first()
        if book:
            uploader_id = book.uploaded_by.id
            if uploader_id == user_id:
                return True, True
            return True, False
        return False, False
    
    def user_fav_book_check(self, user_id, book_id): #  checks if the user has liked the current book
        # Check if there is a different approach
        books = self.filter(user_who_like__id = user_id)
        current_book = self.get(id = book_id)
        for book in books:
            if book == current_book:
                return True
        return False
    
    def process_favorite(self, user_id, book_id, add_to_favorite = True):
        user = Users.objects.get(id= user_id)
        book = self.filter(id = book_id).first()
        if book:
            if add_to_favorite:
                book.user_who_like.add(user)
            else:
                book.user_who_like.remove(user)
        return None
    
    def update_book(self, updated_data, user_id):
        #check if the book with the given id exists and belongs to the current logged in user
        book = self.filter(id = updated_data['book_id'], uploaded_by = Users.objects.get(id = user_id)).first()
        if book:
            book.title = updated_data['book_title']
            book.description = updated_data['book_desc']
            book.save()
        return None

    def delete_book(self, book_id, user_id):
        #check if the book with the given id exists and belongs to the current logged in user
        book = self.filter(id= book_id, uploaded_by = Users.objects.get(id = user_id)).first()
        if book:
            book.delete()
    
        return None


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_by = models.ForeignKey(Users, related_name="books_uploaded", on_delete= models.CASCADE)
    user_who_like = models.ManyToManyField(Users, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BookManager()

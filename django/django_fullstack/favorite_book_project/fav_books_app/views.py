from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.

def render_books_page(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "user" : Users.objects.get(id = request.session['user_id']),
        "books": Book.objects.all()
    }
    return render(request, 'books_home.html', context)

def show_book(request, book_id):
    if request.method == "GET" and 'user_id' in request.session:
        user_id = request.session['user_id']
        book_exists, user_is_uploader = Book.objects.is_uploader(user_id = user_id, book_id = book_id)
        if book_exists:
            
            context = {
                "user": Users.objects.get(id = user_id),
                "book": Book.objects.get(id=book_id),
                "is_user_fav_book" : Book.objects.user_fav_book_check(user_id = user_id, book_id = book_id)
            }
            if user_is_uploader:
                return render(request,'book_edit.html', context)
            else:
                return render(request, 'book_view.html', context)        
    
    return redirect('/')

def add_fav_book(request):
    if request.method == 'POST':
        errors = Book.objects.validate_book(request.POST)
        if errors:
            for key, val in errors.items():
                messages.error(request,val)
        else:
            new_book = Book.objects.add_book(title= request.POST['book_title'], description = request.POST['book_desc'], uploader_id = request.session['user_id'])
        return redirect('/')
    
def process_fav_book(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        book_id = int(request.POST['book_id'])
        if request.POST['action'] == "add_to_fav":
            Book.objects.process_favorite(user_id = user_id, book_id = book_id, add_to_favorite= True)
        elif request.POST['action'] == "remove_from_fav":
            Book.objects.process_favorite(user_id = user_id, book_id = book_id, add_to_favorite= False)

        # if it was a post request redirect to sending page
        return redirect(request.POST['path'])
        
    return redirect('/')

def edit_book(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        if request.POST['action'] == "Update":
            #update book details
            errors = Book.objects.validate_book(request.POST)
            if errors:
                for key, val in errors.items():
                    messages.error(request, val)
            else:
                Book.objects.update_book(updated_data= request.POST, user_id= user_id)
        elif request.POST['action'] == 'Delete':
            #Delete book created by the user
            Book.objects.delete_book(book_id = request.POST['book_id'], user_id = user_id)

    return redirect(f"/books/{request.POST['book_id']}")



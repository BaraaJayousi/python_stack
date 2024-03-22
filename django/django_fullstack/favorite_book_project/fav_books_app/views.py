from django.shortcuts import render, HttpResponse

# Create your views here.

def render_books_page(request):
    return render(request, 'books_home.html')

def show_book(request, book_id):
    if request.method == "GET" and 'user_id' in request.session:
        uploaded_by_id = 2
        if request.session['user_id'] == uploaded_by_id:
            return render(request,'book_edit.html')
        else:
            return render(request, 'book_view.html')

def add_fav_book(request):
    pass

def edit_book(request):
    pass

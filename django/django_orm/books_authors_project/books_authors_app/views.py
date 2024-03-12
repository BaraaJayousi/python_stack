from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def books(request):
    context={
        "books": Books.objects.all()
    }
    return render(request,'books.html', context)

def add_books(request):
    if request.method == 'POST':
        Books.objects.create(title=request.POST['book_title'], desc=request.POST['book_desc'])
    return redirect('/')

def show_book(request, book_id):
    context={
        "book": Books.objects.get(id=book_id),
        "authors": Authors.objects.exclude(books=Books.objects.get(id=book_id))
    }
    return render(request, 'book_details.html', context)


#adds the authors of a specific book
def add_book_author(request, book_id):
    if request.method == 'POST':
        Books.objects.get(id=book_id).authors.add(Authors.objects.get(id=request.POST['book_author']))
        return redirect(f"/books/{book_id}")
    return redirect("/")


def authors(request):
    context = {
        'authors': Authors.objects.all()
    }
    return render(request,'authors.html',context)

def add_author(request):
    if request.method == 'POST':
        Authors.objects.create(first_name =request.POST['f_name'], last_name=request.POST['l_name'], notes=request.POST['author_notes'])
    return redirect('/authors')

def show_author(request, author_id):
    author_details = Authors.objects.get(id=author_id)
    context ={
        'author': author_details,
        'books': Books.objects.exclude(authors= author_details)
    }

    return render(request, 'author_details.html', context)

def add_author_book(request, author_id):
    if request.method == "POST":
        Authors.objects.get(id=author_id).books.add(Books.objects.get(id=request.POST['author_book']))

    return redirect(f"/authors/{author_id}")


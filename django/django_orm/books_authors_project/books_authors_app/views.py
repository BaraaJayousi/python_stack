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

def add_book_author(request, book_id):
    if request.method == 'POST':
        Books.objects.get(id=book_id).authors.add(Authors.objects.get(id=request.POST['book_author']))
        return redirect(f"/books/{book_id}")
    return redirect("/")


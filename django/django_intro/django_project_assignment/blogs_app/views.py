from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.


# def root(request):
#     return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/blogs")


def show(request,number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request,number):
    return redirect('/blogs')

def JSON_data(request):
    data = {"title": "blog title","content": "Ipsum mollit nulla eu exercitation mollit minim duis eu amet excepteur magna in aute. Nostrud minim sunt pariatur consectetur. Duis magna aliquip consequat eiusmod nostrud veniam duis. Exercitation esse sit sint ad excepteur occaecat duis minim laboris cillum cillum exercitation id. Officia elit id anim in pariatur incididunt nostrud enim magna."}
    
    return JsonResponse(data)
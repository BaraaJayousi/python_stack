from django.shortcuts import render, HttpResponse,redirect

# Create your views here.

def user_register(request):
    return HttpResponse('placeholder for users to create a new user record')

def user_login(request):
    return HttpResponse("placeholder for users to log in")

def users_list(request):
    return HttpResponse('placeholder to later display all the list of users')

def blog_redirect(request):
    return redirect('/blogs')
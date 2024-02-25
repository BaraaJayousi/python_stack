from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>This is the equivalent of @app.route('/') in Flask</h1>")

def redirect_view(request):
    return redirect("/redirected_path")

def redirected_view(request):
    return JsonResponse({"response":"JSON response came after redirecting to this path"})
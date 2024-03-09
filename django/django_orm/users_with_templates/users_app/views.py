from django.shortcuts import render, redirect
from .models import Users

from .libs.validators import is_valid_email
# Create your views here.

def index(request):
    if "errors" not in request.session:
        request.session["errors"] = ""
    
    context = {
        "users" : Users.objects.all(),
        "errors": request.session["errors"]
    }
    return render(request,'index.html', context)

def add_user(request):
    if request.method == "POST":
        if is_valid_email(request.POST['email']):
            Users.objects.create(first_name = request.POST["f_name"], last_name = request.POST["l_name"], email= request.POST["email"], age= request.POST["age"])
            del request.session['errors']
        else:
            request.session['errors'] = "Please enter a valid email"
        
    return redirect('/users/')
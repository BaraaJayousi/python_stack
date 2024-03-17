from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def render_form(request):
    return render(request, 'login_register.html')

def register_user(request):
    if request.method == 'POST':
        errors = Users.objects.validate_user(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value, extra_tags="register_error")
            return redirect('/')
        else:
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt(16)).decode()
            new_user = Users.objects.create(first_name = request.POST['f_name'], last_name = request.POST['l_name'], email =request.POST['email'],password= pw_hash)

            request.session['user_id'] = new_user.id

            return redirect('/success')
    else:
        return redirect('/')

def login_user(request):
    if request.method == 'POST':
        user = Users.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]

            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('/success')
        print('no login')
        messages.error(request,"Your email or password is wrong", extra_tags='login_error')
    return redirect('/')

def render_success(request):
    if 'user_id' in request.session:
        context ={
            'user' : Users.objects.get(id=request.session['user_id'])
        }
        return render(request, 'success.html', context)
    else:
        return redirect('/') 
    

def logout_user(request):
    del request.session['user_id']
    return redirect('/')
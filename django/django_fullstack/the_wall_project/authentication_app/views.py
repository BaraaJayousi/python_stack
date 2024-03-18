from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


#render login/register page
def render_authentication_page(request):
    if 'user_id' in request.session:
        return redirect('/wall')
    
    return render(request, 'auth_page.html')

def register_user(request):
    if request.method == 'POST':
        errors = Users.objects.validate_user(request.POST)
        if errors:
            for key, val in errors.items():
                messages.error(request, val,extra_tags='register_error')
        else:
            new_user = Users.objects.create(first_name = request.POST['f_name'], last_name = request.POST['l_name'], email = request.POST['email'], password= Users.objects.hash_user_pw(request.POST['password']))
            request.session['user_id'] = new_user.id

    return redirect('/wall')    

def login_user(request):
    if request.method == 'POST':
        user = Users.objects.filter(email = request.POST['email'])
        if user and Users.objects.check_login_pw(request.POST['password'], user[0]):
                request.session['user_id'] = user[0].id
        else:
            messages.error(request, "your email or password doesn't match",extra_tags='login_error')
    return redirect('/wall')

def logout_user(request):
    del request.session['user_id']    
    return redirect('/wall')
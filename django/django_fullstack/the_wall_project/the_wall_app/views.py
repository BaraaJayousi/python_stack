from django.shortcuts import render, redirect
from authentication_app.models import Users
from .models import *
from django.contrib import messages as flash_msgs
# Create your views here.

def render_main_page(request):
    if 'user_id' in request.session:
        context ={
            'logged_in_user' : Users.objects.get(id=request.session['user_id']),
            'all_messages': Messages.objects.all()
        }
        return render(request, 'main_page.html', context)
    
    return redirect('/auth')

def post_user_message(request):
    if request.method == 'POST':
        if 'user_id' in request.session:
            if int(request.POST['poster_user_id']) == request.session['user_id']:
                Messages.objects.create(user_id = Users.objects.get(id =request.POST['poster_user_id']), message=request.POST['user_message'])
    return redirect('/wall')

def post_user_comment(request):
    if request.method == 'POST':
        if 'user_id' in request.session:
            if int(request.POST['comment_user_id']) == request.session['user_id']:
                Comments.objects.create(message_id= Messages.objects.get(id=request.POST['message_id']), user_id=Users.objects.get(id=request.POST['comment_user_id']), comment= request.POST['user_comment'])
    return redirect('/wall')

def process_message(request):
    if request.method == 'POST':
        if request.POST['action'] == 'delete_message':
            errors =Messages.objects.validate_message_deletion(request.POST['message_id'])
            if errors:
                for key, val in errors.items():
                    flash_msgs.error(request, val,extra_tags='danger')
            else:
                Messages.objects.get(id=request.POST['message_id']).delete()
                flash_msgs.success(request,"Your message has been deleted successfully", extra_tags='success')

            return redirect('/wall')
        elif  request.POST['action'] == 'edit_message':
            pass
    return redirect('/auth')

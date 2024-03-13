from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def render_shows(request):
    context ={
        "shows": TV_shows.objects.all()
    }
    return render(request, 'shows.html', context)

def redirect_to_shows(request):
    return redirect('/shows')

def render_new_show_form(request):
    return render(request, 'new_show.html')

def add_new_show(request):
    if request.method == 'POST':
        new_show = TV_shows.objects.create(title=request.POST['show_title'], network=request.POST['network_name'],notes=request.POST['show_desc'], release_date=request.POST['release_date'])
    return redirect(f"/shows/{new_show.id}")

def show_details(request, show_id):
    context = {
        'show': TV_shows.objects.get(id=show_id)
    }
    return render(request, 'show_details.html', context)

def edit_show(request, show_id):
    context = {
        "show":TV_shows.objects.get(id=show_id)
    }
    return render(request, 'new_show.html', context)

def update_show(request, show_id):
    if request.method == 'POST':
        show = TV_shows.objects.get(id = show_id)
        show.title = request.POST['show_title']
        show.network = request.POST['network_name']
        show.notes = request.POST['show_desc']
        show.release_date = request.POST['release_date']
        show.save()
    return redirect(f'/shows/{show_id}')

def delete_show(request,show_id):
    if request.method == 'POST':
        TV_shows.objects.get(id=show_id).delete()
    return redirect('/')
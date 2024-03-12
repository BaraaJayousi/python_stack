from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def render_shows(request):
    return render(request, 'shows.html')

def render_new_show_form(request):
    return render(request, 'new_show.html')

def add_new_show(request):
    # ToDo: make dynamic ID assignment
    return redirect(f"/shows/1")

def show_details(request, show_id):
    return render(request, 'show_details.html')

def edit_show(request, show_id):
    demo_show = {
        "title": "booklyn 99",
        "network": "HBO",
        "notes":"Ad in nostrud aliqua ullamco. Reprehenderit incididunt quis Lorem quis proident quis officia. Lorem nostrud velit labore non. Laborum fugiat eu duis officia ut. In ut eiusmod veniam laborum proident. Eu esse dolore adipisicing velit proident aliqua velit fugiat culpa laborum exercitation quis."
    }

    context = {
        "show":demo_show
    }
    return render(request, 'new_show.html', context)
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    context = {
        'dojos': Dojos.objects.all(),
        'ninjas': Ninjas.objects.all()
    }
    return render(request, "index.html", context)


def add_ninja(request):
    if request.method == "POST":
        Ninjas.objects.create(dojo =Dojos.objects.get(id= request.POST['selected_dojo']) , first_name= request.POST['ninja_f_name'], last_name= request.POST['ninja_l_name'])
    return redirect('/')

def add_dojo(request):
    if request.method == "POST":
        Dojos.objects.create(name=request.POST['dojo_name'], city=request.POST['dojo_city'], state=request.POST['dojo_state'], desc="New Dojo")

    return redirect('/')
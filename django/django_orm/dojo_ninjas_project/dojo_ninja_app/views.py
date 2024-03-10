from django.shortcuts import render, redirect
from .models import *
from django.db.models import Count

# Create your views here.

def index(request):
    all_dojos = Dojos.objects.all()
    context = {"dojos_list" : []}
    for dojo in all_dojos:
        context['dojos_list'].append({'dojo':dojo, 'ninjas': Ninjas.objects.filter(dojo=dojo)})
    return render(request, "index.html", context)


def add_ninja(request):
    if request.method == "POST":
        Ninjas.objects.create(dojo =Dojos.objects.get(id= request.POST['selected_dojo']) , first_name= request.POST['ninja_f_name'], last_name= request.POST['ninja_l_name'])
    return redirect('/')

def add_dojo(request):
    if request.method == "POST":
        Dojos.objects.create(name=request.POST['dojo_name'], city=request.POST['dojo_city'], state=request.POST['dojo_state'], desc="New Dojo")

    return redirect('/')

def delete_dojo(request):
    if request.method == "POST":
        Dojos.objects.get(id=request.POST['dojo_to_delete']).delete()
    return redirect('/')
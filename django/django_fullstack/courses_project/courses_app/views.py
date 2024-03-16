from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def render_courses(request):
    context ={
        "courses": Courses.objects.all()
    }
    return render(request, 'courses_page.html', context)

def add_course(request):
    if request.method == "POST":
        errors = Courses.objects.validate_courses(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request,value) 
        else:
            Courses.objects.create(name=request.POST['course_name'], description = request.POST['course_desc'])
    return redirect('/')

def destroy_course(request, course_id):
    context = {
        'course': Courses.objects.get(id = course_id)
    }
    if request.method == "GET":
        return render(request, 'destroy_course.html', context)
    
    if request.method == 'POST':
        context['course'].delete()
        return redirect('/')

from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    context = {
        "dojo_locations":['San Jose', 'New York', 'New Jersey', 'Ohio','Los Santos']
    }
    return render(request, 'index.html', context)

def result(request):
    if request.method == 'POST':
        print(request.POST)
        context={
            "username":request.POST['username'],
            "email": request.POST['email'],
            "dojo_location": request.POST['dojo_location'],
            "comments": request.POST['comments']
        }
        return render(request, 'result.html', context)

    return redirect('/')
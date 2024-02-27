from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if "count" not in request.session or "visits" not in request.session:
        request.session['increment_val'] = 1
        request.session['count'] = -1
        request.session['visits'] = -1

    request.session['count'] += request.session['increment_val'] 
    request.session['visits'] += 1
    context ={"counter": request.session['count'],
                "visits": request.session['visits']}
    return render(request,"index.html", context)


def counter_actions(request):
    if request.method == 'POST':
        if request.POST['action'] == "destroy_session":
            request.session.flush()
        if request.POST['action'] == "increment_two":
            request.session['count'] += (2- request.session['increment_val'] )
        if request.POST['action'] == "custom_increment":
            request.session['increment_val'] = int(request.POST['increment_value'])
    return redirect('/')
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if "count" not in request.session:
        request.session['count'] = -1
    request.session['count'] += 1
    context ={"counter": request.session['count']}
    return render(request,"index.html", context)


def destroy_session(request):
    request.session.flush()
    return redirect('/')

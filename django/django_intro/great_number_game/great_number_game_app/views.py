from django.shortcuts import render, redirect
import random

# Create your views here.

def index(request):
    if 'random_num' not in request.session:
        return redirect('/reset-game')
    
    context = {"result":request.session['guess_result'],
                "color": (lambda result: result == 'correct' and 'success' or 'danger')(request.session['guess_result']),
                }
    print(context['color'])

    return render(request, 'index.html', context)

def check_answer(request):
    if request.method == "POST":
        if int(request.POST['guess']) > request.session['random_num']:
            request.session['guess_result'] ='high'
        elif int(request.POST['guess']) < request.session['random_num']:
            request.session['guess_result'] ='low'
        else:
            request.session['guess_result'] ='correct'
    return redirect('/')

def reset_game(request):
    request.session['random_num'] = random.randint(1,100)
    request.session['guess_result'] =''
    return redirect('/')
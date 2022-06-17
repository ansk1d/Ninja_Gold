from django.shortcuts import render, redirect
import random

def index(request):
    if 'mygold' not in request.session:
        request.session['mygold'] =0
    context = {
        "gold" :request.session['mygold']
    }
    return render(request, "index.html", context)

def findgold(request):
    randomnum = random.randint(10,20)
    request.session['mygold']+=randomnum
    return redirect('/')

def luckgold(request):
    randomnum = random.randint(-50,50)
    request.session['mygold']+=randomnum
    return redirect('/')
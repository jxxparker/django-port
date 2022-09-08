from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from time import strftime, localtime

def index(request):
    return render(request, "apps/index.html")

def addWord(request):
    if request.POST['word'] == ' ':
        messages.add_message(request, messages.ERROR, "Word can't be blank!")
        return redirect('/')
    
    if "words" not in request.session:
        request.session['words'] = []
        print("Blank session")

    if "bigfont" in request.POST:
        data = {
            "word": request.POST['word'],
            "color": request.POST['color'],
            "font": 'big',
        }
    else:
        data = {
            "word": request.POST['word'],
            "color": request.POST['color'],
            "font": 'small',
        }
    
    request.session['words'].append(data)
    request.session.modified = True
    return redirect('/')

def clear(request):
    print("--SESSION CLEARED!--")
    request.session.clear()
    return redirect('/')
    



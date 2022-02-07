from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime
from datetime import datetime, timezone


def index(request):
    content = {
        'date' : strftime("%b %d, %Y", gmtime()),
        'time' : strftime('%I:%M %p', gmtime())
    }
    return render(request, "apps/index.html", content)



    

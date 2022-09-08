from django.shortcuts import render, redirect
from django.http import HttpResponse
import random

def index(request):
    if "money" not in request.session:
        request.session["money"] = 0
    if "action" not in request.session:
        request.session["action"] = []
    return render(request, "apps/index.html")

def process(request):
    if request.method == "POST":
        if request.POST["hidden"] == "lightBet":
            check_win = random.randint(0, 1)
            if check_win == 1:
                found = random.randrange(5,20)
                request.session["money"] += found
                request.session["action"].append("WON LIGHT BET : You WON $" + str(found))
            else:
                found = random.randrange(5,20)
                request.session["money"] -= found
                request.session["action"].append("LOST LIGHT BET: You LOST $" + str(found))
        
        if request.POST["hidden"] == "mediumBet":
            check_win = random.randint(0, 1)
            if check_win == 1:
                found = random.randrange(10,25)
                request.session["money"] += found
                request.session["action"].append("WON MEDIUM BET : You WON $" + str(found))
            else:
                found = random.randrange(10,25)
                request.session["money"] -= found
                request.session["action"].append("LOST medium BET: You LOST $" + str(found))

        if request.POST["hidden"] == "highBet":
            check_win = random.randint(0, 1)
            if check_win == 1:
                found = random.randrange(20,50)
                request.session["money"] += found
                request.session["action"].append("WON HIGH BET : You WON $" + str(found))
            else:
                found = random.randrange(20,50)
                request.session["money"] -= found
                request.session["action"].append("LOST HIGH BET: You LOST $" + str(found))

        if request.POST["hidden"] == "superhighBet":
            check_win = random.randint(0, 1)
            if check_win == 1:
                found = random.randrange(50,100)
                request.session["money"] += found
                request.session["action"].append("WON SUPER HIGH : You WON $" + str(found))
            else:
                found = random.randrange(50,100)
                request.session["money"] -= found
                request.session["action"].append("LOST SUPER HIGH : You LOST $" + str(found))
        return redirect('/')

def clear(request):
    if request.method == "POST":
        del request.session["money"]
        del request.session["action"]
        return redirect('/')
    else:
        return redirect("/")
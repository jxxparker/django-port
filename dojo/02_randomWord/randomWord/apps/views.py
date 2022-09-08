from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
import random


def randomizers(request):
    if "random_count" not in request.session.keys():
        request.session["random_count"] = 0
    else:
        request.session["random_count"] += 1
    
    context = {
        "random_count": request.session["random_count"],
        "random_number": random.randint(10, 99),
        "random_str": get_random_string(length=10),
    }

    return render(request, "apps/index.html", context)

# def reset(request):
#     request.session["random_count"] = 0
#     return render(request, "apps/index.html")






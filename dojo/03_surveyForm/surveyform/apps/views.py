from django.shortcuts import render, redirect 
from django.http import HttpResponse

def index(request):
    return render(request, "apps/index.html")

def create_user(request):
    name_survey = request.POST['name']
    location_survey = request.POST['location']
    language_survey = request.POST['language']
    comments = request.POST['description']

    context = {
        "name_template" : name_survey,
        "location_template" : location_survey,
        "language_template" : language_survey,
        "comments" : comments,
    }
    return render(request, "apps/result.html", context)



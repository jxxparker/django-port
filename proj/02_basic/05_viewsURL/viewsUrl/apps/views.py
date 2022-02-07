from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HttpResponse("Projects page worked.")

def product(request, pk):
    return HttpResponse("this page will work with whatever word after THIS" + " " + str(pk))
from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'main.html')

def projects(request):
    return render(request, 'apps/projects.html')

def singles(request, pk):
    return render(request, 'apps/singles.html')
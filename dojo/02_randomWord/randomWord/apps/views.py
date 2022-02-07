from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if request.method == 'POST':
        unique_id = get_random_string(length=16)
        
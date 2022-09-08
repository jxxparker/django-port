from django.shortcuts import render, redirect

def profiles(request):
    return render(request, "apps/profiles.html")

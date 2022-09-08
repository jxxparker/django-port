from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required


def loginUser(request):
    
    if request.user.is_authenticated:
        return redirect("profiles")


    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profiles")
        else:
            messages.error(request, "Username OR password is incorrect")

    return render(request, "users/loginRegis.html")


def logoutUser(request):
    logout(request)
    messages.error(request, "Username was logged out")
    return redirect("loginUser")


def profiles(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, "users/profiles.html", context)


def userProfile(request, pk):
    userProfile = Profile.objects.get(id=pk)
    topSkills = userProfile.skill_set.exclude(description__exact="")
    otherSkills = userProfile.skill_set.filter(description="")

    context = {
        "userProfile": userProfile, 
        "topSkills": topSkills, 
        "otherSkills": otherSkills
    }
    return render(request, "users/userProfile.html", context)
    

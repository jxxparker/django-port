import re
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Tag
from .forms import ProjectForm
from .utils import searchProjects, paginateProjects
from django.core import paginator


def index(request):
    projects, search_query = searchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 3)

    context = {
        "projects": projects, 
        "search_query": search_query, 
        "paginator": paginator, 
        "custom_range": custom_range
    }

    return render(request, "apps/index.html", context)

def display(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, "apps/display.html", {"projectObj": projectObj})

@login_required(login_url="login")
def create(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid(): #checks if everything is valid
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect("userAccount")

    context = {"form": form}
    return render(request, "apps/crud.html", context)

@login_required(login_url="login")    
def update(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid(): #checks if everything is valid
            form.save()
            return redirect("userAccount")

    context = {"form": form}
    return render(request, "apps/crud.html", context)

@login_required(login_url="login")    
def delete(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("index")
    context = {"project_name": project}
    return render(request, "delete.html", context)


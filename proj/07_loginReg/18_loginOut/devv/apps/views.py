from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

def index(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "apps/index.html", context)

def display(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, "apps/display.html", {"projectObj": projectObj})

@login_required(login_url="login")
def create(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid(): #checks if everything is valid
            form.save()
            return redirect("index")

    context = {"form": form}
    return render(request, "apps/crud.html", context)

@login_required(login_url="login")    
def update(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid(): #checks if everything is valid
            form.save()
            return redirect("index")

    context = {"form": form}
    return render(request, "apps/crud.html", context)

@login_required(login_url="login")    
def delete(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("index")
    context = {"project_name": project}
    return render(request, "apps/delete.html", context)


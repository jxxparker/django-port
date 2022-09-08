from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

def index(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, 'apps/index.html', context)

def display(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, "apps/display.html", {"projects": projectObj, "tags": tags})


def createProject(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    
    context = {"form": form}
    return render(request, "apps/create_update.html", context)

def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("index")
    
    context = {"form": form}
    return render(request, "apps/create_update.html", context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("index")
    context = {"object": project}
    return render(request, "apps/delete.html", context)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

def projects(request):
    # page = "this is page"        
    # number = 10
    projects = Project.objects.all()
    # context = {"page": page, "number": number, 'projects': projectsList}
    context = {"projects": projects}
    return render(request, 'apps/projects.html', context)

def singles(request, pk):
    # projectObj = None
    # for i in projectsList:
    #     if i['id'] == pk:
    #         projectObj = i
    # return render(request, "apps/singles.html", {"project": projectObj})

    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, "apps/singles.html", {"projects": projectObj, "tags": tags})

def createProject(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("projects")


    context = {"form": form}
    return render(request, "apps/project_form.html", context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")


    context = {"form": form}
    return render(request, "apps/project_form.html", context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects")
    context = {"object": project}
    return render(request, "apps/delete_template.html", context)





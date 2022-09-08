from multiprocessing import context
from struct import pack_into
from django.shortcuts import render
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
    return render(request, "apps/singles.html", {"project": projectObj, "tags": tags})

def createProject(request):
    form = ProjectForm()
    context = {"form": form}
    return render(request, "apps/project_form.html", context)








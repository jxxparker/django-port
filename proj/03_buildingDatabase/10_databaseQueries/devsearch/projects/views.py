from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectsList = [
    {
        "id": "1",
        "title": "Eccomerce Website",
        "description": "Fully functional ecomerce website"
    },
    {
        "id": "2",
        "title": "Portfolio Website",
        "description": "This was project where I built out for my portoflio"
    },
    {
        "id": "3",
        "title": "Social Network",
        "description": "Awesome open source projects that is being worked on."
    },
]

def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, 'projects/projects.html', context)


def single_project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single_project.html', {"project": projectObj})

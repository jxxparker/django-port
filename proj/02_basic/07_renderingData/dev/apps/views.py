from django.shortcuts import render
from django.http import HttpResponse

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
    page = "this is page"        
    number = 10
    context = {"page": page, "number": number, 'projects': projectsList}
    return render(request, 'apps/projects.html', context)

def singles(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, "apps/singles.html", {"project": projectObj})




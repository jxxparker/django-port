from django.urls import path, include
from projects import views

urlpatterns =[
    path("", views.projects, name="projects"),
    path("singleProject/<str:pk>", views.single_project, name="singleProject"),
    path("createProject/", views.createProject, name="createProject"),
    path("updateProject/<str:pk>", views.updateProject, name="updateProject"),
    path("deleteProject/<str:pk>", views.deleteProject, name="deleteProject"),
]
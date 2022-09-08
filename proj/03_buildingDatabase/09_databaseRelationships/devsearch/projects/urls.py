from django.urls import path, include
from projects import views

urlpatterns =[
    path("", views.projects, name="projects"),
    path("single_project/<str:pk>", views.single_project, name="single_project")
]
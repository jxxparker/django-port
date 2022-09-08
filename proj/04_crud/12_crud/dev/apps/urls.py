from django.urls import path
from apps import views

urlpatterns =[
    path('', views.projects, name="projects"),
    path('singles/<str:pk>', views.singles, name="singles"),
    path('createproject/', views.createProject, name="createproject"),
    path('updateproject/<str:pk>/', views.updateProject, name="updateproject"),
    path('deleteproject/<str:pk>/', views.deleteProject, name="deleteproject")
]
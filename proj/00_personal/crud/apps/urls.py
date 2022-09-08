from apps import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('display/<str:pk>', views.display, name="display"),
    path('createproject/', views.createProject, name="createproject"),
    path('updateproject/<str:pk>/', views.updateProject, name="updateproject"),
    path('deleteproject/<str:pk>/', views.deleteProject, name="deleteproject"),
    
]
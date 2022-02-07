from django.urls import path
from apps import views

urlpatterns = [
    path('', views.index, name="index"),
    path('project/<str:pk>', views.project, name="project")
]


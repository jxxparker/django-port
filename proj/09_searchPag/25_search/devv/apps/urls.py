from django.urls import path, include
from apps import views

urlpatterns = [
    path("", views.index, name="index"),
    path("display/<str:pk>", views.display, name="display"),
    path("crud/", views.create, name="create"),
    path("update/<str:pk>", views.update, name="update"),
    path("delete/<str:pk>", views.delete, name="delete"),
]




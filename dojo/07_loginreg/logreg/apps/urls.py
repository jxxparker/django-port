from django.urls import path, include
from apps import views

urlpatterns = [
    path('', views.profiles, name="profiles")
]
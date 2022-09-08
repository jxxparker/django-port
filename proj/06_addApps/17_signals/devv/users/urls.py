from django.urls import path, include
from users import views

urlpatterns = [
    path("", views.profiles, name="profiles"),
    path("userProfile/<str:pk>", views.userProfile, name="userProfile"),
]

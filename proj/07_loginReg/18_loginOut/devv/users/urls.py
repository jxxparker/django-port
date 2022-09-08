from django.urls import path, include
from users import views

urlpatterns = [
    path("loginUser/", views.loginUser, name="loginUser"),
    path("logoutUser/", views.logoutUser, name="logoutUser"),

    path("", views.profiles, name="profiles"),
    path("userProfile/<str:pk>", views.userProfile, name="userProfile"),
]

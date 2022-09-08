from django.urls import path, include
from users import views

urlpatterns = [
    path("loginUser/", views.loginUser, name="loginUser"),
    path("logoutUser/", views.logoutUser, name="logoutUser"),
    path("registerUser/", views.registerUser, name="registerUser"),

    path("", views.profiles, name="profiles"),
    path("userProfile/<str:pk>", views.userProfile, name="userProfile"),
    path("userAccount/", views.userAccount, name="userAccount"),
    path("editAccount/", views.editAccount, name="editAccount")
]

from django.urls import path, include
from users import views

urlpatterns = [
    path("loginUser/", views.loginUser, name="loginUser"),
    path("logoutUser/", views.logoutUser, name="logoutUser"),
    path("registerUser/", views.registerUser, name="registerUser"),

    path("", views.profiles, name="profiles"),
    path("userProfile/<str:pk>", views.userProfile, name="userProfile"),
    path("userAccount/", views.userAccount, name="userAccount"),
    path("editAccount/", views.editAccount, name="editAccount"),
    path("createSkill/", views.createSkill, name="createSkill"),
    path("updateSkill/<str:pk>", views.updateSkill, name="updateSkill"),
    path("deleteSkill/<str:pk>", views.deleteSkill, name="deleteSkill"),
]


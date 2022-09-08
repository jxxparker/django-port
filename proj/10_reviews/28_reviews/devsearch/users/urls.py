from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    
    path('', views.profiles, name="profiles"),
    path('userProfile/<str:pk>', views.userProfile, name="user_profile"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('account/', views.userAccount, name="account"),
    path('editAccount', views.editAccount, name="edit_account"),
    path('createSkill', views.createSkill, name="create_skill"),
    path('updateSkill/<str:pk>', views.updateSkill, name="update_skill"),
    path('deleteSkill/<str:pk>', views.deleteSkill, name="delete_skill"),
]

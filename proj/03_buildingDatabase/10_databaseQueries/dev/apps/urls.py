from django.urls import path
from apps import views

urlpatterns =[
    path('', views.projects, name="projects"),
    path('singles/<str:pk>', views.singles, name="singles"),
    #<str:pk> this means you can put your own str
]
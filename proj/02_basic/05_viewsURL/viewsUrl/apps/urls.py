from django.urls import path
from apps import views

urlpatterns = [
    path('projects/', views.projects, name="projects"),
    path('product/<str:pk>', views.product, name="product"), 
    #<str:pk> this means you can put your own str
]
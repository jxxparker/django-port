from django.urls import path
from . import views

urlpatterns = [
    path('', views.randomizers),    
    path('randomizer', views.randomizers), 
]
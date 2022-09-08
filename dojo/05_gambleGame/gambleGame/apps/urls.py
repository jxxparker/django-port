from django.urls import path
from apps import views

urlpatterns = [
    path('', views.index, name="index"),
    path('clear', views.clear, name="clear"),
    path('process', views.process, name="process"),
]
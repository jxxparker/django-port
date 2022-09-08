from xml.dom.pulldom import IGNORABLE_WHITESPACE
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('addWord', views.addWord, name="addWord"),
    path('clear', views.clear, name="clear")
]


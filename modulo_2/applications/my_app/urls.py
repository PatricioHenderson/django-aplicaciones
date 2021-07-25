#from modulo_2.applications import my_app
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    
    path('', views.endpoint),
]
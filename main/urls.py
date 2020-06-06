from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/home', views.home, name='home'),
    path('logout', views.logoutUser, name='logoutUser'),
]

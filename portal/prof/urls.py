from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.add_student, name='add_student')
]
from django.urls import path
from . import views

urlpatterns = [
    path('<str:prof_username>/students', views.view_students, name='view_students'),
]
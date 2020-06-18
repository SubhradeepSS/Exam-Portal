from django.urls import path
from . import views

urlpatterns = [
    path('<str:prof_username>/question', views.add_question, name='add_question'),
    path('<str:prof_username>/question/view_all_ques', views.view_all_ques, name='view_all_ques'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('<str:prof_username>/exams', views.view_exams, name='view_exams'),
    path('<str:prof_username>/exams/<int:exam_id>', views.view_exam, name='view_exam'),
    path('<str:prof_username>/exams/<int:exam_id>/edit', views.edit_exam, name='edit_exam'),
    path('<str:prof_username>/exams/<int:exam_id>/delete', views.delete_exam, name='delete_exam'),
]
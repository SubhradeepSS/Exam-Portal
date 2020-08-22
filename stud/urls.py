from django.urls import path
from . import views

app_name = 'stud'

urlpatterns = [
    path('<int:stud_username>', views.index, name='index'),
    path('<int:stud_username>/exams', views.view_exams, name='view_exams'),
]

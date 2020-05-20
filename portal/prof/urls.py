from django.urls import path
from . import views

app_name = 'prof'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.add_student, name='add_student'),
    path('question', views.add_question, name='add_question')
]
from django.urls import path
from . import views

app_name = 'prof'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.add_student, name='add_student'),
    path('question', views.add_question, name='add_question'),
    path('questionpaper', views.make_paper ,name='make_paper') ,
    path('questionpaper/addquestion',views.add_question_in_paper, name="add_question_in_paper"),
    path('questionpaper/viewpaper',views.view_paper,name='view_paper')
]
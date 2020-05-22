from django.urls import path
from . import views

app_name = 'prof'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.add_student, name='add_student'),
    path('question', views.add_question, name='add_question'),
    path('questionpaper', views.make_paper ,name='make_paper') ,
    path('questionpaper/addquestion',views.add_question_in_paper, name="add_question_in_paper"),
    path('questionpaper/viewpaper',views.view_paper,name='view_paper'),
    path('login/viewgroups', views.create_student_group, name='view_groups'),
    path('login/viewgroups/<int:group_id>', views.view_specific_group, name='view_specific_group'),
    path('login/viewgroups/<int:group_id>/students', views.view_student_in_group, name='view_students_in_group'),
    path('login/viewgroups/<int:group_id>/questions', views.view_question_in_group, name='view_questions_in_group'),
    path('login/viewgroups/<int:group_id>/question_papers', views.view_questionpaper_in_group, name='view_questionpaper_in_group')
]
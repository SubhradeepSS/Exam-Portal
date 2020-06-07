from django.urls import path
from . import views

app_name = 'prof'

urlpatterns = [
                            # PROF HOME
    path('<str:prof_username>', views.index, name='index'),
    # path('<str:prof_username>/loginProf', views.loginProf, name='loginProf'),
    # path('logoutProf', views.logoutProf, name='logoutProf'),

                            # EXAM
    path('<str:prof_username>/exams', views.view_exams, name='view_exams'),
    path('<str:prof_username>/exams/<int:exam_id>', views.view_exam, name='view_exam'),
    path('<str:prof_username>/exams/<int:exam_id>/edit', views.edit_exam, name='edit_exam'),
    path('exams/<int:exam_id>/delete', views.delete_exam, name='delete_exam'),
    # path('login', views.add_student, name='add_student'),
    # path('login/students', views.view_students, name='view_students'),

                            # QUESTION
    path('<str:prof_username>/question', views.add_question, name='add_question'),
    path('<str:prof_username>/question/view_all_ques', views.view_all_ques, name='view_all_ques'),

                            # QUESTION PAPER
    path('<str:prof_username>/questionpaper', views.make_paper ,name='make_paper') ,
    path('<str:prof_username>/questionpaper/addquestion',views.add_question_in_paper, name="add_question_in_paper"),
    path('<str:prof_username>/questionpaper/viewpaper',views.view_paper,name='view_paper'),
    path('<str:prof_username>/questionpaper/editpaper',views.edit_paper,name='edit_paper'),
    path('<str:prof_username>/questionpaper/viewpaper/<int:paper_id>', views.view_specific_paper, name='view_specific_paper'),
    path('<str:prof_username>/question/view_all_ques/edit_question/<int:ques_qno>',views.edit_question,name="edit_question"),
    
                            # STUDENT GROUP
    path('<str:prof_username>/viewgroups', views.create_student_group, name='view_groups'),
    path('<str:prof_username>/viewgroups/<int:group_id>', views.view_specific_group, name='view_specific_group'),
    path('<str:prof_username>/viewgroups/<int:group_id>/students', views.view_student_in_group, name='view_students_in_group'),
    path('<str:prof_username>/viewgroups/<int:group_id>/questions', views.view_question_in_group, name='view_questions_in_group'),
    path('<str:prof_username>/viewgroups/<int:group_id>/question_papers', views.view_questionpaper_in_group, name='view_questionpaper_in_group'),
    path('<str:prof_username>/viewgroups/<int:group_id>/delete', views.delete_group, name='delete_group'),
]
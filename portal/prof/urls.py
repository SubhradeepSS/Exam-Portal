from django.urls import path
from . import views

app_name = 'prof'
urlpatterns = [
    path('', views.index, name='index'),
    path('exams', views.view_exams, name='view_exams'),
    path('exams/<int:exam_id>', views.view_exam, name='view_exam'),
    path('exams/<int:exam_id>/edit', views.edit_exam, name='edit_exam'),
    path('exams/<int:exam_id>/delete', views.delete_exam, name='delete_exam'),
    path('login', views.add_student, name='add_student'),
    path('login/students', views.view_students, name='view_students'),
    path('question', views.add_question, name='add_question'),
    path('question/view_all_ques', views.view_all_ques, name='view_all_ques'),
    path('questionpaper', views.make_paper ,name='make_paper') ,
    path('questionpaper/addquestion',views.add_question_in_paper, name="add_question_in_paper"),
    path('questionpaper/viewpaper',views.view_paper,name='view_paper'),
    path('questionpaper/editpaper',views.edit_paper,name='edit_paper'),
    path('questionpaper/viewpaper/<int:paper_id>', views.view_specific_paper, name='view_specific_paper'),
    path('login/viewgroups', views.create_student_group, name='view_groups'),
    path('login/viewgroups/<int:group_id>', views.view_specific_group, name='view_specific_group'),
    path('login/viewgroups/<int:group_id>/students', views.view_student_in_group, name='view_students_in_group'),
    path('login/viewgroups/<int:group_id>/questions', views.view_question_in_group, name='view_questions_in_group'),
    path('login/viewgroups/<int:group_id>/question_papers', views.view_questionpaper_in_group, name='view_questionpaper_in_group'),
    path('login/viewgroups/<int:group_id>/delete', views.delete_group, name='delete_group'),
    path('question/view_all_ques/edit_question/<int:ques_qno>',views.edit_question,name="edit_question") 
]
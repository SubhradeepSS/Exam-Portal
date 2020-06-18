from django.urls import path
from . import views

urlpatterns = [
    path('<str:prof_username>/questionpaper', views.make_paper ,name='make_paper') ,
    path('<str:prof_username>/questionpaper/addquestion',views.add_question_in_paper, name="add_question_in_paper"),
    path('<str:prof_username>/questionpaper/viewpaper',views.view_paper,name='view_paper'),
    path('<str:prof_username>/questionpaper/editpaper',views.edit_paper,name='edit_paper'),
    path('<str:prof_username>/questionpaper/viewpaper/<int:paper_id>', views.view_specific_paper, name='view_specific_paper'),
    path('<str:prof_username>/question/view_all_ques/edit_question/<int:ques_qno>',views.edit_question,name="edit_question"),
]
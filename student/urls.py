from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
                                # HOME
    path('<str:stud_username>', views.index, name='index'),
    
                                # EXAM
    path('<str:stud_username>/exam', views.exam, name='exam'),
    path('<str:stud_username>/results', views.results, name='results')
    # path('login', views.loginStud, name='loginStud'),
    # path('logout', views.logoutStud, name='logoutStud'),
]

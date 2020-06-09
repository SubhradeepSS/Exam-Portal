from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
    # HOME
    path('<str:stud_username>', views.index, name='index'),
    path('<str:stud_username>/exam', views.exam, name='exam')
    # path('login', views.loginStud, name='loginStud'),
    # path('logout', views.logoutStud, name='logoutStud'),
]

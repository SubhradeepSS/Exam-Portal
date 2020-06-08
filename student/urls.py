from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginStud, name='loginStud'),
    path('logout', views.logoutStud, name='logoutStud'),
]
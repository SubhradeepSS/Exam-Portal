from django.shortcuts import render
from main.models import *
from django.contrib.auth.models import User

def view_students(request, prof_username):
    return render(request, 'prof/student/view_students.html', {
        'students': User.objects.filter(groups__name='Student'),
        'prof': User.objects.get(username=prof_username)
    })
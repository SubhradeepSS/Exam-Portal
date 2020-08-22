from django.shortcuts import render
from main.models import *
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def view_students(request, prof_username):
    if request.user == prof:
        return render(request, 'prof/student/view_students.html', {
            'students': User.objects.filter(groups__name='Student'),
            'prof': User.objects.get(username=prof_username)
        })
    else:
        return HttpResponseForbidden("You are not allowed to view this page. Please change url to original values to return.")
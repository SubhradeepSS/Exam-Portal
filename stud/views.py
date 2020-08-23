from django.shortcuts import render
from django.http import request, HttpResponse, HttpResponseForbidden
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def index(request, stud_username):
    stud = User.objects.get(username=stud_username)

    if request.user == stud:
        return render(request, 'stud/index.html', {
            'stud': stud
        })
    else:
        return HttpResponseForbidden("You are not allowed to view this page. Please press back button to return.")


def view_exams(request, stud_username):
    stud = User.objects.get(username=stud_username)

    if request.user == stud:
        groups = stud.group.all()
        exams = set()
        for group in groups:
            group_exams = group.exam
            for exam in group_exams.all():
                
                exams.add(exam)

        return render(request, 'stud/view_exams.html', {
            'stud': stud, 'exams': list(exams)
        })
    else:
        return HttpResponseForbidden("You are not allowed to view this page. Please press back button to return.")


def view_exam(request, stud_username, exam_id):
    pass
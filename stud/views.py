from django.shortcuts import render
from django.http import request, HttpResponse, HttpResponseForbidden
from django.contrib.auth.models import User

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
        exams = []
        for group in groups:
            group_exams = group.exam
            for exam in group_exams:
                if exam not in exams:
                    exams.append(exam)

        return render(request, 'stud/view_exams.html', {
            'stud': stud, 'exams': exams
        })
    else:
        return HttpResponseForbidden("You are not allowed to view this page. Please press back button to return.")       
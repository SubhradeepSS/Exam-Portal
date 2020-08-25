from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from main.models import *
from django.contrib.auth.models import User
from student.models import *

def results(request, stud_username):
    student = User.objects.get(username=stud_username)

    if request.user == student:
        studentGroup = Special_Students.objects.filter(students=student)
        studentExamList = StuExam_DB.objects.filter(student=student, completed=1)
        if request.method == 'POST':
            paper = request.POST['paper']
            viewExam = StuExam_DB.objects.get(examname=paper, student=student)
            return render(request, 'student/result/individualresult.html', {
                'exam': viewExam,
                'student': student,
                'quesn': viewExam.questions.all()
            })
        return render(request, 'student/result/results.html', {
            'student': student,
            'paper': studentExamList
        })
    else:
        return HttpResponseForbidden("You are not allowed to view this page. Please change url to original values to return.")
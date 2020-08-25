from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from main.models import *
from django.contrib.auth.models import User
from student.models import *

from .exams import *
from .result import *

# Create your views here.

def index(request, stud_username):
    student = User.objects.get(username=stud_username)

    if request.user == student:
        studentGroup = Special_Students.objects.filter(students=student)
        examsList = []
        if studentGroup.exists():
            for i in studentGroup:
                b = Exam_Model.objects.filter(student_group=i)
                if b.exists():
                    if b.count() > 1:
                        for j in b:
                            examsList.append(j)
                    else:
                        examsList.append(Exam_Model.objects.get(student_group=i))
        if examsList != []:
            for i in examsList:
                currentExamList = StuExam_DB.objects.filter(
                    examname=i.name, student=student)
                if currentExamList.exists() != True:  # If no exam are there in then add exams
                    tempExam = StuExam_DB(student=student, examname=i.name,
                                        qpaper=i.question_paper, score=0, completed=0)
                    tempExam.save()
                    temp1 = i.question_paper
                    temp2 = temp1.questions.all()
                    for ques in temp2:
                        # add all the questions from the prof to student database
                        studentQuestion = Stu_Question(question=ques.question, optionA=ques.optionA, optionB=ques.optionB,
                                                    optionC=ques.optionC, optionD=ques.optionD,
                                                    answer=ques.answer, student=student)
                        studentQuestion.save()
                        tempExam.questions.add(studentQuestion)
        return render(request, 'student/index.html', {
            'stud': student
        })
    
    else:
        return HttpResponseForbidden("You are not allowed to view this page. Please change url to original values to return.")
from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import *
from django.contrib.auth.models import User
from .models import *
# Create your views here.


def index(request, stud_username):
    student = User.objects.get(username=stud_username)
    return render(request, 'student/index.html', {
        'stud': student
    })


def exam(request, stud_username):
    student = User.objects.get(username=stud_username)
    a = Special_Students.objects.filter(students=student)
    c = []
    if a.exists():
        for i in a:
            b = Exam_Model.objects.filter(student_group=i)
            if b.exists():
                if b.count() > 1:
                    for j in b:
                        c.append(j)
                else:
                    c.append(Exam_Model.objects.get(student_group=i))
    if request.method == 'POST' and request.POST.get('papertitle', False) == False:
        paper = request.POST['paper']
        e = Exam_Model.objects.get(name=paper)
        f = e.question_paper
        g = f.questions.all()
        l = Stu_Question.objects.filter(student=student)
        l.delete()
        for ques in g:
            a = Stu_Question(question=ques.question, optionA=ques.optionA, optionB=ques.optionB,
                             optionC=ques.optionC, optionD=ques.optionD,
                             answer=ques.answer, student=student)
            a.save()
        return render(request, 'student/viewpaper.html', {
            'qpaper': f,
            'question_list': Stu_Question.objects.filter(student=student),
            'student': student,
            'exam': paper
        })
    elif request.method == 'POST' and request.POST.get('papertitle', False) != False:
        paper = request.POST['paper']
        title = request.POST['papertitle']
        e = Exam_Model.objects.get(name=paper)
        f = e.question_paper
        g = f.questions.all()
        l = Stu_Question.objects.filter(student=student)
        h = 0
        for ques in l:
            ans = request.POST[ques.question]
            ques.choice = ans
            ques.save()
            if ans == ques.answer:
                h = h + 1
        return render(request, 'student/result.html', {
            'Title': title,
            'Score': h,
            'student': student
        })
    return render(request, 'student/viewexam.html', {
        'student': student,
        'paper': c
    })
# def loginStud(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect("student:index")
#         else:
#             return redirect("student:loginStud")

#     return render(request,"student/login.html")

# def logoutStud(request):
#     logout(request)
#     return redirect('student:loginStud')

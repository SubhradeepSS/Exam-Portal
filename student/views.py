from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import *
from django.contrib.auth.models import User
from .models import *
# Create your views here.


def index(request, stud_username):
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
    if c != []:
        for i in c:
            abc = StuExam_DB.objects.filter(examname=i.name, student=student)
            if abc.exists() != True:
                d = StuExam_DB(student=student, examname=i.name,
                               qpaper=i.question_paper, score=0, completed=0)
                d.save()
                e = i.question_paper
                j = e.questions.all()
                for ques in j:
                    az = Stu_Question(question=ques.question, optionA=ques.optionA, optionB=ques.optionB,
                                      optionC=ques.optionC, optionD=ques.optionD,
                                      answer=ques.answer, student=student)
                    az.save()
                    d.questions.add(az)
                # d.save()
    return render(request, 'student/index.html', {
        'stud': student
    })


def exam(request, stud_username):
    student = User.objects.get(username=stud_username)
    a = Special_Students.objects.filter(students=student)
    c = StuExam_DB.objects.filter(student=student)
    if request.method == 'POST' and request.POST.get('papertitle', False) == False:
        paper = request.POST['paper']
        e = StuExam_DB.objects.get(examname=paper, student=student)
        f = e.qpaper
        #g = f.questions.all()
        h = e.questions.all().delete()
        j = f.questions.all()
        for ques in j:
            az = Stu_Question(question=ques.question, optionA=ques.optionA, optionB=ques.optionB,
                              optionC=ques.optionC, optionD=ques.optionD,
                              answer=ques.answer, student=student)
            az.save()
            e.questions.add(az)
            e.save()
        e.completed = 1
        e.save()
        return render(request, 'student/viewpaper.html', {
            'qpaper': f,
            'question_list': e.questions.all(),
            'student': student,
            'exam': paper
        })
    elif request.method == 'POST' and request.POST.get('papertitle', False) != False:
        paper = request.POST['paper']
        title = request.POST['papertitle']
        e = StuExam_DB.objects.get(examname=paper)
        f = e.qpaper
        #g = f.questions.all()
        #h = e.questions.all().delete()
        l = e.questions.all()
        h = 0
        for ques in l:
            ans = request.POST[ques.question]
            ques.choice = ans
            ques.save()
            if ans == ques.answer:
                h = h + 1
        e.score = h
        e.save()
        return render(request, 'student/result.html', {
            'Title': title,
            'Score': h,
            'student': student
        })
    return render(request, 'student/viewexam.html', {
        'student': student,
        'paper': c
    })


def results(request, stud_username):
    student = User.objects.get(username=stud_username)
    a = Special_Students.objects.filter(students=student)
    c = StuExam_DB.objects.filter(student=student, completed=1)
    if request.method == 'POST':
        paper = request.POST['paper']
        e = StuExam_DB.objects.get(examname=paper, student=student)
        return render(request, 'student/individualresult.html', {
            'exam': e,
            'student': student,
            'quesn': e.questions.all()
        })
    return render(request, 'student/results.html', {
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

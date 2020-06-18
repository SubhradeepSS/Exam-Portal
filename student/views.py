from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import *
from django.contrib.auth.models import User
from .models import *
from django.utils import timezone

# Create your views here.

def index(request, stud_username):
    student = User.objects.get(username=stud_username)
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


def exam(request, stud_username):
    student = User.objects.get(username=stud_username)
    studentGroup = Special_Students.objects.filter(students=student)
    studentExamsList = StuExam_DB.objects.filter(student=student)
    if request.method == 'POST' and request.POST.get('papertitle', False) == False:

        paper = request.POST['paper']
        stuExam = StuExam_DB.objects.get(examname=paper, student=student)
        qPaper = stuExam.qpaper
        examMain = Exam_Model.objects.get(name=paper)
        #g = f.questions.all()

        # TIME COMPARISON
        exam_start_time = examMain.start_time
        curr_time = timezone.now()

        if curr_time < exam_start_time:
            return redirect('student:exam', stud_username)

        h = stuExam.questions.all().delete()
        qPaperQuestionsList = qPaper.questions.all()
        for ques in qPaperQuestionsList:
            temp = Stu_Question(question=ques.question, optionA=ques.optionA, optionB=ques.optionB,
                                optionC=ques.optionC, optionD=ques.optionD,
                                answer=ques.answer, student=student)
            temp.save()
            stuExam.questions.add(temp)
            stuExam.save()
        stuExam.completed = 1
        stuExam.save()
        mins = examMain.duration
        secs = 0 
        return render(request, 'student/viewpaper.html', {
            'qpaper': qPaper,
            'question_list': stuExam.questions.all(),
            'student': student,
            'exam': paper ,
            'min' : mins ,
            'sec' : secs
        })
    elif request.method == 'POST' and request.POST.get('papertitle', False) != False:
        paper = request.POST['paper']
        title = request.POST['papertitle']
        
        stuExam = StuExam_DB.objects.get(examname=paper, student=student)
        qPaper = stuExam.qpaper
        #g = f.questions.all()
        #h = e.questions.all().delete()
        examQuestionsList = stuExam.questions.all()
        examScore = 0
        for ques in examQuestionsList:
            ans = request.POST.get(ques.question,False)
            if ans == False :
                ans = "E"
            ques.choice = ans
            ques.save()
            if ans == ques.answer:
                examScore = examScore + 1
        stuExam.score = examScore
        stuExam.save()
        a=6000
        return render(request, 'student/result.html', {
            'Title': title,
            'Score': examScore,
            'student': student
        })
    return render(request, 'student/viewexam.html', {
        'student': student,
        'paper': studentExamsList,
    })


def results(request, stud_username):
    student = User.objects.get(username=stud_username)
    studentGroup = Special_Students.objects.filter(students=student)
    studentExamList = StuExam_DB.objects.filter(student=student, completed=1)
    if request.method == 'POST':
        paper = request.POST['paper']
        viewExam = StuExam_DB.objects.get(examname=paper, student=student)
        return render(request, 'student/individualresult.html', {
            'exam': viewExam,
            'student': student,
            'quesn': viewExam.questions.all()
        })
    return render(request, 'student/results.html', {
        'student': student,
        'paper': studentExamList
    })

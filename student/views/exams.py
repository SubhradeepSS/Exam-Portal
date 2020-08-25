from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from main.models import *
from django.contrib.auth.models import User
from student.models import *
from django.utils import timezone

def exams(request, stud_username):
    student = User.objects.get(username=stud_username)

    if request.user == student:
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
                return redirect('student:exams', stud_username)

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
            return render(request, 'student/paper/viewpaper.html', {
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
            return render(request, 'student/result/result.html', {
                'Title': title,
                'Score': examScore,
                'student': student
            })
        return render(request, 'student/exam/viewexam.html', {
            'student': student,
            'paper': studentExamsList,
        })
    else:
        return HttpResponseForbidden("You are not allowed to view this page. Please change url to original values to return.")
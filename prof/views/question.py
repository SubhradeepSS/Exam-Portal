from django.shortcuts import render, redirect
from main.models import *
from django.contrib.auth.models import User

def add_question(request, prof_username):
    prof = User.objects.get(username=prof_username)

    if request.method == 'POST':
        form = QForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.professor = prof
            form.save()
            return redirect('prof:view_all_ques', prof_username=prof_username)

    return render(request, 'prof/question/question.html', {
        'question_db': Question_DB.objects.filter(professor=prof),
        'form': QForm(), 'prof': prof
    })


def view_all_ques(request, prof_username):
    prof = User.objects.get(username=prof_username)

    if request.method == 'POST':
        ano = request.POST['qno']
        ano = int(ano)
        # Question_DB.objects.get(qno=ano).delete()
        sum = 1
        for i in Question_DB.objects.filter(professor=prof):
            sum += 1
            l = i.qno
        c = ano
        d = int(c)+1
        e = []
        for i in range(d, sum):
            f = Question_DB.objects.filter(professor=prof, qno=int(i)).first()
            # e.append(Question_DB.objects.get(qno=int(i)))
            f.qno -= 1
            f.save()
        sum -= 1

        Question_DB.objects.filter(professor=prof, qno=l).delete()

    return render(request, 'prof/question/view_all_questions.html', {
        'question_db': Question_DB.objects.filter(professor=prof), 'prof': prof
    })


def edit_question(request, prof_username, ques_qno):
    prof = User.objects.get(username=prof_username)
    ques = Question_DB.objects.get(professor=prof, qno=ques_qno)
    form = QForm(instance=ques)

    if request.method == "POST":
        form = QForm(request.POST, instance=ques)
        if form.is_valid():
            # form = form.save(commit=False)
            # form.professor = prof
            form.save()
            # return render(request,'prof/edit_question.html',{
            # 'i' : Question_DB.objects.filter(professor=prof,qno=ques_qno) ,
            # 'form':form
            # })
            return redirect('prof:view_all_ques', prof_username=prof_username)

    return render(request, 'prof/question/edit_question.html', {
        'i': Question_DB.objects.filter(professor=prof, qno=ques_qno).first(),
        'form': form, 'prof': prof
    })
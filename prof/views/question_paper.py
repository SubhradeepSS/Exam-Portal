from django.shortcuts import render, redirect
from main.models import *
from django.contrib.auth.models import User

def make_paper(request, prof_username):
    prof = User.objects.get(username=prof_username)

    if request.method == 'POST' and request.POST.get('presence', False) == False:
        add_question_in_paper(request, prof_username)

    elif request.method == 'POST' and request.POST.get('presence', False) != False:
        title = request.POST['title']
        a = Question_Paper.objects.filter(
            professor=prof, qPaperTitle=title).first()
        a.delete()

    return render(request, 'prof/question_paper/qpaper.html', {
        'qpaper_db': Question_Paper.objects.filter(professor=prof), 'prof': prof
    })


def add_question_in_paper(request, prof_username):
    prof = User.objects.get(username=prof_username)

    if request.method == 'POST' and request.POST.get('qpaper', False) != False:
        paper_title = request.POST['qpaper']
        question_paper = Question_Paper(
            professor=prof, qPaperTitle=paper_title)
        question_paper.save()
        left_ques = []
        for i in Question_DB.objects.filter(professor=prof):
            if i not in question_paper.questions.all():
                left_ques.append(i)
        return render(request, 'prof/question_paper/addquestopaper.html', {
            'qpaper': question_paper,
            'question_list': left_ques, 'prof': prof
        })

    elif request.method == 'POST' and request.POST.get('title', False) != False:
        addques = request.POST['title']
        a = Question_DB.objects.filter(professor=prof, qno=addques).first()
        title = request.POST['papertitle']
        b = Question_Paper.objects.filter(
            professor=prof, qPaperTitle=title).first()
        b.questions.add(a)
        b.save()
        left_ques = []
        for i in Question_DB.objects.filter(professor=prof):
            if i not in b.questions.all():
                left_ques.append(i)
        return render(request, 'prof/question_paper/addquestopaper.html', {
            'qpaper': b,
            'question_list': left_ques, 'prof': prof
        })

    return render(request, 'prof/question_paper/addquestopaper.html')


def view_paper(request, prof_username):
    prof = User.objects.get(username=prof_username)

    if request.method == 'POST':
        papertitle = request.POST['title']
        b = Question_Paper.objects.get(
            professor=prof, qPaperTitle=papertitle)

        return render(request, 'prof/question_paper/viewpaper.html', {
            'qpaper': b,
            'question_list': b.questions.all(), 'prof': prof
        })


def edit_paper(request, prof_username):
    prof = User.objects.get(username=prof_username)

    if request.method == 'POST' and request.POST.get('title', False) != False:
        papertitle = request.POST['title']
        b = Question_Paper.objects.filter(
            professor=prof, qPaperTitle=papertitle).first()
        left_ques = []
        for i in Question_DB.objects.filter(professor=prof):
            if i not in b.questions.all():
                left_ques.append(i)
        return render(request, 'prof/question_paper/editpaper.html', {
            'ques_left': left_ques,
            'qpaper': b,
            'question_list': b.questions.all(), 'prof': prof
        })

    elif request.method == 'POST' and request.POST.get('remove', False) != False:
        papertitle = request.POST['paper']
        no = request.POST['question']
        b = Question_Paper.objects.filter(
            professor=prof, qPaperTitle=papertitle).first()
        a = Question_DB.objects.filter(professor=prof, qno=no).first()
        b.questions.remove(a)
        b.save()
        left_ques = []
        for i in Question_DB.objects.filter(professor=prof):
            if i not in b.questions.all():
                left_ques.append(i)
        return render(request, 'prof/question_paper/editpaper.html', {
            'ques_left': left_ques,
            'qpaper': b,
            'question_list': b.questions.all(), 'prof': prof
        })

    elif request.method == 'POST' and request.POST.get('qnumber', False) != False:
        qno = request.POST['qnumber']
        ptitle = request.POST['titlepaper']
        b = Question_Paper.objects.filter(
            professor=prof, qPaperTitle=ptitle).first()
        a = Question_DB.objects.filter(professor=prof, qno=qno).first()
        b.questions.add(a)
        b.save()
        left_ques = []
        for i in Question_DB.objects.filter(professor=prof):
            if i not in b.questions.all():
                left_ques.append(i)

        return render(request, 'prof/question_paper/editpaper.html', {
            'ques_left': left_ques,
            'qpaper': b,
            'question_list': b.questions.all(), 'prof': prof
        })


def view_specific_paper(request, prof_username, paper_id):
    prof = User.objects.get(username=prof_username)
    paper = Question_Paper.objects.get(professor=prof, pk=paper_id)

    return render(request, 'prof/question_paper/viewpaper.html', {
        'qpaper': paper, 'question_list': paper.questions.all(), 'prof': prof
    })
from django.shortcuts import render, redirect
from main.models import *
from django.contrib.auth.models import User

def view_exams(request, prof_username):
    prof = User.objects.get(username=prof_username)
    new_Form = ExamForm()
    new_Form.fields["student_group"].queryset = Special_Students.objects.filter(
        professor=prof)
    new_Form.fields["question_paper"].queryset = Question_Paper.objects.filter(
        professor=prof)

    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.professor = prof
            exam.save()
            form.save_m2m()
            return redirect('prof:view_exams', prof_username=prof_username)

    exams = Exam_Model.objects.filter(professor=prof)

    return render(request, 'prof/exam/view_exams.html', {
        'exams': exams, 'examform': new_Form, 'prof': prof,
    })


def view_exam(request, prof_username, exam_id):
    prof = User.objects.get(username=prof_username)
    exam = Exam_Model.objects.get(professor=prof, pk=exam_id)
    return render(request, 'prof/exam/view_exam.html', {
        'exam': exam, 'prof': prof, 'student_group': exam.student_group.all()
    })


def edit_exam(request, prof_username, exam_id):
    prof = User.objects.get(username=prof_username)
    exam = Exam_Model.objects.filter(professor=prof, pk=exam_id).first()
    new_Form = ExamForm(instance=exam)
    new_Form.fields["student_group"].queryset = Special_Students.objects.filter(
        professor=prof)
    new_Form.fields["question_paper"].queryset = Question_Paper.objects.filter(
        professor=prof)

    if request.method == 'POST':
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            return redirect('prof:view_exams', prof_username=prof_username)

    return render(request, 'prof/exam/edit_exam.html', {
        'form': new_Form, 'exam': exam, 'prof': prof
    })


def delete_exam(request, prof_username, exam_id):
    prof = User.objects.get(username=prof_username)
    exam = Exam_Model.objects.get(professor=prof, pk=exam_id)
    exam.delete()
    return redirect('prof:view_exams', prof_username=prof_username)
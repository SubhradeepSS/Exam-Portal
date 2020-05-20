from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Student, Question_DB

# Create your views here.
def index(request):
    return render(request, 'prof/index.html')

def add_student(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        student = Student(username=username, password=password)
        student.save()
        
    return render(request, 'prof/add.html',{
        'student_db': Student.objects.all()
    })

def add_question(request):
    if request.method == 'POST':
        question = request.POST['question']
        answer = request.POST['answer']
        ques = Question_DB(question=question, answer=answer)
        ques.save()
        
    return render(request, 'prof/question.html',{
        'question_db': Question_DB.objects.all()
    })
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Student, Question_DB , Question_Paper

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
        optiona = request.POST['optiona']
        optionb = request.POST['optionb']
        optionc = request.POST['optionc']
        optiond = request.POST['optiond']
        answer = request.POST['answer']
        ques = Question_DB(question=question, optionA=optiona ,optionB=optionb,optionC=optionc,optionD=optiond,answer=answer)
        ques.save()
        
    return render(request, 'prof/question.html',{
        'question_db': Question_DB.objects.all()
    })
def make_paper(request) :
    if request.method=='POST' :
        add_question_in_paper(request)
    return render(request, 'prof/qpaper.html',{
        'qpaper_db' : Question_Paper.objects.all()
    } ) 

def add_question_in_paper(request) :
    if request.method =='POST'  and request.POST.get('qpaper', False) != False :
        paper_title =request.POST['qpaper']
        question_paper=Question_Paper(qPaperTitle=paper_title)
        question_paper.save()
        return render(request,'prof/addquestopaper.html' , {
            'qpaper' : question_paper ,
            'question_list' : Question_DB.objects.all()
        })
    elif request.method == 'POST' :
        addques = request.POST['title']
        a = Question_DB.objects.get(qno=addques)
        title = request.POST['papertitle']
        b = Question_Paper.objects.get(qPaperTitle=title)
        b.questions.add(a)
        return render(request,'prof/addquestopaper.html' , {
            'qpaper' : b ,
            'question_list' : Question_DB.objects.all()
        })
        
    return render(request,'prof/addquestopaper.html' )

def view_paper(request) :
    if request.method == 'POST' :
        papertitle=request.POST['title']
        b = Question_Paper.objects.get(qPaperTitle=papertitle)
        return render(request,'prof/viewpaper.html' , {
            'qpaper' : b ,
            'question_list' : b.questions.all()
        })
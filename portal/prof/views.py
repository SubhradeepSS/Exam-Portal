from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Student, Question_DB , Question_Paper, Special_Students

# Create your views here.
def index(request):
    return render(request, 'prof/index.html', {
        'special_students_db': Special_Students.objects.all()
    })

def add_student(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        student = Student(username=username, password=password)
        student.save()
        return render(request, 'prof/view_all_students.html',{
            'students_db': Student.objects.all()
        })
        
    return render(request, 'prof/add.html')

def view_students(request):
    return render(request, 'prof/view_all_students.html',{
        'students_db': Student.objects.all()
    })

# def delete_student_fromDB(request, student_id):
#     Student.objects.filter(pk=student_id).delete()
#     return render(request, 'prof/add.html')

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

c=[]
def make_paper(request) :
    if request.method=='POST' :
        add_question_in_paper(request)
        
    return render(request, 'prof/qpaper.html',{
        'qpaper_db' : Question_Paper.objects.all()
    } ) 
c=[]
def add_question_in_paper(request) :
    d=[]
    for i in Question_DB.objects.all() :
        d.append(i)
    if request.method =='POST'  and request.POST.get('qpaper', False) != False :
        paper_title =request.POST['qpaper']
        question_paper=Question_Paper(qPaperTitle=paper_title)
        question_paper.save()
        while c != [] :
            c.pop()
        return render(request,'prof/addquestopaper.html' , {
            'qpaper' : question_paper ,
            'question_list' : Question_DB.objects.all()
        })
    elif request.method == 'POST' and request.POST.get('title', False) != False : 
        addques = request.POST['title']
        a = Question_DB.objects.get(qno=addques)
        title = request.POST['papertitle']
        b = Question_Paper.objects.get(qPaperTitle=title)
        b.questions.add(a)
        # if a in d :
        #     d.remove(a)
        c.append(a)
        return render(request,'prof/addquestopaper.html' , {
            'qpaper' : b ,
            'question_list' : d,
            'elist' : c
        })
    while c != [] :
        c.pop()
    return render(request,'prof/addquestopaper.html' )

def view_paper(request) :
    if request.method == 'POST' :
        papertitle=request.POST['title']
        b = Question_Paper.objects.get(qPaperTitle=papertitle)
        return render(request,'prof/viewpaper.html' , {
            'qpaper' : b ,
            'question_list' : b.questions.all()
        })

def view_specific_paper(request, paper_id):
    paper = Question_Paper.objects.get(pk=paper_id)
    return render(request, 'prof/viewpaper.html',{
        'qpaper': paper, 'question_list': paper.questions.all()
    })

def create_student_group(request):
    if request.method == 'POST':
        category = Special_Students(category_name=request.POST['category_name'])
        category.save()

    return render(request, 'prof/addview_groups.html', {
        'special_students_db': Special_Students.objects.all()
    })


def view_specific_group(request, group_id):
    group = Special_Students.objects.get(pk=group_id)
    return render(request, 'prof/view_specific_group.html', {
        'group': group
    })

def view_student_in_group(request, group_id):
    group = Special_Students.objects.get(pk=group_id)
    if request.method == 'POST':
        student_username = request.POST['username']
        student = Student.objects.get(username=student_username)
        group.students.add(student)

    return render(request, 'prof/view_special_stud.html',{
        'students': group.students.all(), 'group': group
    })

def view_question_in_group(request, group_id):
    group = Special_Students.objects.get(pk=group_id)

    if request.method == 'POST':
        question_no = request.POST['question_no']
        question = Question_DB.objects.get(qno=question_no)
        group.questions.add(question)

    return render(request, 'prof/view_ques_in_group.html',{
        'group': group, 'all_questions':Question_DB.objects.all(),
        'questions_in_group': group.questions.all()
    })


def view_questionpaper_in_group(request, group_id):
    group = Special_Students.objects.get(pk=group_id)

    if request.method == 'POST':
        qpaper_title = request.POST['qpaper_title']
        qpaper = Question_Paper.objects.get(qPaperTitle = qpaper_title)
        group.question_papers.add(qpaper)
    
    return render(request, 'prof/view_qpaper_in_group.html',{
        'group':group, 'all_qpapers': Question_Paper.objects.all(),
        'qpapers_in_group': group.question_papers.all()
    })

def delete_group(request, group_id):
    Special_Students.objects.filter(pk=group_id).delete()
    
    return render(request, 'prof/addview_groups.html', {
        'special_students_db': Special_Students.objects.all()
    })
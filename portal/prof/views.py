from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Student, Question_DB , Question_Paper, Special_Students , QNO, Exam_Model, ExamForm
from django.contrib.auth import login,logout,authenticate
# from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect("prof:loginProf")
    return render(request, 'prof/index.html', {
        'special_students_db': Special_Students.objects.all()
    })

def loginProf(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("prof:index")
        else:
            return redirect("prof:loginProf")
    
    return render(request,"prof/login.html")

def logoutProf(request):
    logout(request)
    return redirect("prof:loginProf")

def view_exams(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'prof/view_exams.html',{
        'exams': Exam_Model.objects.all(), 'examform': ExamForm()
    })

def view_exam(request, exam_id):
    exam = Exam_Model.objects.get(pk=exam_id)
    return render(request, 'prof/view_exam.html',{
        'exam': exam
    })


def edit_exam(request, exam_id):
    exam = Exam_Model.objects.get(pk=exam_id)
    exm_form = ExamForm(instance=exam)
    
    if request.method == 'POST':
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            return render(request, 'prof/view_exam.html',{
                'exam': exam
            })
    return render(request, 'prof/edit_exam.html',{
        'form': exm_form, 'exam':exam
    })

def delete_exam(request, exam_id):
    exam = Exam_Model.objects.get(pk=exam_id)
    exam.delete()
    return redirect('prof:view_exams')

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
    if request.method=='POST' :
        username=request.POST['username']
        a=Student.objects.get(username=username)
        a.delete()
    return render(request, 'prof/view_all_students.html',{
        'students_db': Student.objects.all()
    })

# def delete_student_fromDB(request, student_id):
#     Student.objects.filter(pk=student_id).delete()
#     return render(request, 'prof/add.html')

def add_question(request):
    if request.method == 'POST' and request.POST.get('question', False) != False :
        question = request.POST['question']
        optiona = request.POST['optiona']
        optionb = request.POST['optionb']
        optionc = request.POST['optionc']
        optiond = request.POST['optiond']
        answer = request.POST['answer']
        ques = Question_DB(question=question, optionA=optiona ,optionB=optionb,optionC=optionc,optionD=optiond,answer=answer)
        
        a=QNO.objects.get(nid=1)
        a.number+=1
        a.nid=1
        a.save()
        ques.qno=a.number
        ques.save()
    return render(request, 'prof/question.html',{
        'question_db': Question_DB.objects.all() ,
    })


def view_all_ques(request):
    if request.method=='POST' :
        ano = request.POST['qno']
        ano=int(ano)
        #Question_DB.objects.get(qno=ano).delete()
        sum=1
        for i in Question_DB.objects.all() :
            sum+=1
            l=i.qno
        c=ano
        d=int(c)+1
        e=[]
        for i in range(d,sum) :
            f=Question_DB.objects.get(qno=int(i))
            #e.append(Question_DB.objects.get(qno=int(i)))
            f.qno-=1
            f.save()
        sum-=1
        Question_DB.objects.get(qno=l).delete()    
        a=QNO.objects.get(nid=1)
        a.number-=1
        a.nid=1
        a.save()
    return render(request, 'prof/view_all_questions.html',{
        'question_db': Question_DB.objects.all() ,
    })

def make_paper(request) :
    if request.method=='POST' and request.POST.get('presence', False) == False:
        add_question_in_paper(request)
    elif request.method=='POST' and request.POST.get('presence', False) != False:    
        title = request.POST['title']
        a=Question_Paper.objects.get(qPaperTitle=title)
        a.delete()
    return render(request, 'prof/qpaper.html',{
        'qpaper_db' : Question_Paper.objects.all()
    } ) 
    
def add_question_in_paper(request) :
    
    if request.method =='POST'  and request.POST.get('qpaper', False) != False :
        paper_title =request.POST['qpaper']
        question_paper=Question_Paper(qPaperTitle=paper_title)
        question_paper.save()
        left_ques=[]
        for i in Question_DB.objects.all():
            if i not in question_paper.questions.all():
                left_ques.append(i)
        return render(request,'prof/addquestopaper.html' , {
            'qpaper' : question_paper ,
            'question_list' : left_ques
        })
    elif request.method == 'POST' and request.POST.get('title', False) != False : 
        addques = request.POST['title']
        a = Question_DB.objects.get(qno=addques)
        title = request.POST['papertitle']
        b = Question_Paper.objects.get(qPaperTitle=title)
        b.questions.add(a)
        b.save()
        left_ques=[]
        for i in Question_DB.objects.all():
            if i not in b.questions.all():
                left_ques.append(i)
        return render(request,'prof/addquestopaper.html' , {
            'qpaper' : b ,
            'question_list' : left_ques
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

def edit_paper(request) :
    if request.method == 'POST' and request.POST.get('title', False) != False :
        papertitle=request.POST['title']
        b = Question_Paper.objects.get(qPaperTitle=papertitle)
        left_ques=[]
        for i in Question_DB.objects.all():
            if i not in b.questions.all():
                left_ques.append(i)
        return render(request,'prof/editpaper.html' , {
            'ques_left' : left_ques ,
            'qpaper' : b ,
            'question_list' : b.questions.all()
        }) 
    elif request.method == 'POST' and request.POST.get('remove', False) != False :
        papertitle=request.POST['paper']
        no=request.POST['question']
        b = Question_Paper.objects.get(qPaperTitle=papertitle)
        a=Question_DB.objects.get(qno=no)
        b.questions.remove(a)
        b.save()
        left_ques=[]
        for i in Question_DB.objects.all():
            if i not in b.questions.all():
                left_ques.append(i)
        return render(request,'prof/editpaper.html' , {
            'ques_left' : left_ques ,
            'qpaper' : b ,
            'question_list' : b.questions.all()
        })  
    elif request.method == 'POST' and request.POST.get('qnumber', False) != False :
        qno=request.POST['qnumber']
        ptitle=request.POST['titlepaper']
        b = Question_Paper.objects.get(qPaperTitle=ptitle)
        a = Question_DB.objects.get(qno=qno)
        b.questions.add(a)
        b.save()
        left_ques=[]
        for i in Question_DB.objects.all():
            if i not in b.questions.all():
                left_ques.append(i)
        return render(request,'prof/editpaper.html' , {
            'ques_left' : left_ques ,
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

def edit_question(request,ques_qno):
    ques = Question_DB.objects.get(qno=ques_qno)
    if request.method =="POST" :
        t=Question_DB.objects.get(qno=ques_qno)
        question = request.POST['question']
        optiona = request.POST['optiona']
        optionb = request.POST['optionb']
        optionc = request.POST['optionc']
        optiond = request.POST['optiond']
        answer = request.POST['answer']
        n=request.POST['number']
        Question_DB.objects.get(qno=n).delete()
        
        t1 = Question_DB(qno=n,question=question, optionA=optiona ,optionB=optionb,optionC=optionc,optionD=optiond,answer=answer)
        t1.save()
    return render(request,'prof/edit_question.html',{
        'i' : Question_DB.objects.get(qno=ques_qno)
    })

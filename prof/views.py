from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from main.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
# from django.contrib.auth.models import User

# Create your views here.
def index(request,prof_username):
    prof = User.objects.get(username=prof_username)
    return render(request, 'prof/index.html',{
        'prof':prof
    })

def view_students(request, prof_username):
    return render(request, 'prof/view_students.html', {
        'students': User.objects.filter(groups__name='Student')
    })

# def loginProf(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             return redirect("prof:index")
#         else:
#             return redirect("prof:loginProf")
    
#     return render(request,"prof/login.html")

# def logoutProf(request):
#     logout(request)
#     return redirect("prof:loginProf")

def view_exams(request,prof_username):
    prof = User.objects.get(username=prof_username)
    new_Form = ExamForm()
    new_Form.fields["student_group"].queryset = Special_Students.objects.filter(professor=prof)
    new_Form.fields["question_paper"].queryset = Question_Paper.objects.filter(professor=prof)
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.professor = prof
            form.save()

    return render(request, 'prof/view_exams.html',{
        'exams': Exam_Model.objects.filter(professor=prof), 'examform': new_Form, 'prof':prof
    })

def view_exam(request,prof_username, exam_id):
    prof = User.objects.get(username=prof_username)
    exam = Exam_Model.objects.filter(professor=prof,pk=exam_id).first()
    return render(request, 'prof/view_exam.html',{
        'exam': exam, 'prof':prof, 'student_group': exam.student_group.all()
    })

def edit_exam(request,prof_username, exam_id):
    prof = User.objects.get(username=prof_username)
    exam = Exam_Model.objects.filter(professor=prof,pk=exam_id).first()
    exm_form = ExamForm(instance=exam)
    
    if request.method == 'POST':
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            return redirect('prof:view_exam', prof_username=prof_username, exam_id=exam_id)
            
    return render(request, 'prof/edit_exam.html',{
        'form': exm_form, 'exam':exam, 'prof':prof
    })

def delete_exam(request,prof_username, exam_id):
    prof = User.objects.get(username=prof_username)
    exam = Exam_Model.objects.filter(professor=prof,pk=exam_id).first()
    exam.delete()
    return redirect('prof:view_exams', prof_username=prof_username)

# def add_student(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()

#     return render(request, 'prof/add.html',{
#         'form':StudentForm()
#     })

# def view_students(request):
#     if request.method=='POST' :
#         username=request.POST['username']
#         a=Student.objects.get(username=username)
#         a.delete()
#     return render(request, 'prof/view_all_students.html',{
#         'students_db': Student.objects.all()
#     })

# def delete_student_fromDB(request, student_id):
#     Student.objects.filter(pk=student_id).delete()
#     return render(request, 'prof/add.html')

def add_question(request,prof_username):
    prof = User.objects.get(username=prof_username)
    if request.method == 'POST':
        form = QForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.professor = prof
            form.save()
            return redirect('prof:view_all_ques', prof_username=prof_username)
            
    return render(request, 'prof/question.html',{
        'question_db': Question_DB.objects.filter(professor=prof) ,
        'form':QForm(), 'prof':prof
    })


def view_all_ques(request, prof_username):
    prof = User.objects.get(username=prof_username)
    if request.method=='POST' :
        ano = request.POST['qno']
        ano=int(ano)
        #Question_DB.objects.get(qno=ano).delete()
        sum=1
        for i in Question_DB.objects.filter(professor=prof) :
            sum+=1
            l=i.qno
        c=ano
        d=int(c)+1
        e=[]
        for i in range(d,sum) :
            f=Question_DB.objects.filter(professor=prof,qno=int(i)).first()
            #e.append(Question_DB.objects.get(qno=int(i)))
            f.qno-=1
            f.save()
        sum-=1
        Question_DB.objects.filter(professor=prof,qno=l).delete()    
    return render(request, 'prof/view_all_questions.html',{
        'question_db': Question_DB.objects.filter(professor=prof), 'prof':prof
    })


def edit_question(request,prof_username,ques_qno):
    prof = User.objects.get(username=prof_username)
    ques = Question_DB.objects.filter(professor=prof,qno=ques_qno).first()
    form = QForm(instance=ques)
    if request.method =="POST" :
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

    return render(request,'prof/edit_question.html',{
        'i' : Question_DB.objects.filter(professor=prof,qno=ques_qno).first() ,
        'form':form, 'prof':prof
    })


def make_paper(request, prof_username):
    prof = User.objects.get(username=prof_username)

    if request.method=='POST' and request.POST.get('presence', False) == False:
        add_question_in_paper(request, prof_username)

    elif request.method=='POST' and request.POST.get('presence', False) != False:    
        title = request.POST['title']
        a=Question_Paper.objects.filter(professor=prof,qPaperTitle=title).first()
        a.delete()

    return render(request, 'prof/qpaper.html',{
        'qpaper_db' : Question_Paper.objects.filter(professor=prof), 'prof':prof
    } ) 
    
def add_question_in_paper(request, prof_username) :
    prof = User.objects.get(username=prof_username)

    if request.method =='POST'  and request.POST.get('qpaper', False) != False :
        paper_title = request.POST['qpaper']
        question_paper=Question_Paper(professor=prof,qPaperTitle=paper_title)
        question_paper.save()
        left_ques=[]
        for i in Question_DB.objects.filter(professor=prof):
            if i not in question_paper.questions.all():
                left_ques.append(i)
        return render(request,'prof/addquestopaper.html' , {
            'qpaper' : question_paper ,
            'question_list' : left_ques, 'prof':prof
        })

    elif request.method == 'POST' and request.POST.get('title', False) != False : 
        addques = request.POST['title']
        a = Question_DB.objects.filter(professor=prof,qno=addques).first()
        title = request.POST['papertitle']
        b = Question_Paper.objects.filter(professor=prof,qPaperTitle=title).first()
        b.questions.add(a)
        b.save()
        left_ques=[]
        for i in Question_DB.objects.filter(professor=prof):
            if i not in b.questions.all():
                left_ques.append(i)
        return render(request,'prof/addquestopaper.html' , {
            'qpaper' : b ,
            'question_list' : left_ques, 'prof':prof
        })

    return render(request,'prof/addquestopaper.html' )

def view_paper(request, prof_username):
    prof = User.objects.get(username=prof_username)
    if request.method == 'POST' :
        papertitle=request.POST['title']
        b = Question_Paper.objects.filter(professor=prof,qPaperTitle=papertitle).first()
        return render(request,'prof/viewpaper.html' , {
            'qpaper' : b ,
            'question_list' : b.questions.all(), 'prof':prof
        })

def edit_paper(request, prof_username) :
    prof = User.objects.get(username=prof_username)
    if request.method == 'POST' and request.POST.get('title', False) != False :
        papertitle=request.POST['title']
        b = Question_Paper.objects.filter(professor=prof,qPaperTitle=papertitle).first()
        left_ques=[]
        for i in Question_DB.objects.filter(professor=prof):
            if i not in b.questions.all():
                left_ques.append(i)
        return render(request,'prof/editpaper.html' , {
            'ques_left' : left_ques ,
            'qpaper' : b ,
            'question_list' : b.questions.all(), 'prof':prof
        }) 

    elif request.method == 'POST' and request.POST.get('remove', False) != False :
        papertitle = request.POST['paper']
        no = request.POST['question']
        b = Question_Paper.objects.filter(professor=prof,qPaperTitle=papertitle).first()
        a = Question_DB.objects.filter(professor=prof,qno=no).first()
        b.questions.remove(a)
        b.save()
        left_ques=[]
        for i in Question_DB.objects.filter(professor=prof):
            if i not in b.questions.all():
                left_ques.append(i)
        return render(request,'prof/editpaper.html' , {
            'ques_left' : left_ques ,
            'qpaper' : b ,
            'question_list' : b.questions.all(), 'prof':prof
        })  

    elif request.method == 'POST' and request.POST.get('qnumber', False) != False :
        qno = request.POST['qnumber']
        ptitle = request.POST['titlepaper']
        b = Question_Paper.objects.filter(professor=prof,qPaperTitle=ptitle).first()
        a = Question_DB.objects.filter(professor=prof,qno=qno).first()
        b.questions.add(a)
        b.save()
        left_ques=[]
        for i in Question_DB.objects.filter(professor=prof):
            if i not in b.questions.all():
                left_ques.append(i)

        return render(request,'prof/editpaper.html' , {
            'ques_left' : left_ques ,
            'qpaper' : b ,
            'question_list' : b.questions.all(), 'prof':prof
        })  
        
def view_specific_paper(request,prof_username, paper_id):
    prof = User.objects.get(username=prof_username)
    paper = Question_Paper.objects.filter(professor=prof,pk=paper_id).first()
    return render(request, 'prof/viewpaper.html',{
        'qpaper': paper, 'question_list': paper.questions.all(), 'prof':prof
    })

def create_student_group(request, prof_username):
    prof = User.objects.get(username=prof_username)
    if request.method == 'POST':
        category = Special_Students(professor=prof,category_name=request.POST['category_name'])
        category.save()

    return render(request, 'prof/addview_groups.html', {
        'special_students_db': Special_Students.objects.filter(professor=prof), 'prof':prof
    })

def view_specific_group(request,prof_username, group_id):
    prof = User.objects.get(username=prof_username)
    group = Special_Students.objects.filter(professor=prof,pk=group_id).first()
    return render(request, 'prof/view_specific_group.html', {
        'group': group, 'prof':prof
    })

def view_student_in_group(request,prof_username, group_id):
    prof = User.objects.get(username=prof_username)
    group = Special_Students.objects.filter(professor=prof,pk=group_id).first()
    if request.method == 'POST':
        student_username = request.POST['username']
        student = User.objects.get(username=student_username)
        group.students.add(student)

    return render(request, 'prof/view_special_stud.html',{
        'students': group.students.all(), 'group': group, 'prof':prof
    })

# def view_question_in_group(request,prof_username, group_id):
#     prof = User.objects.get(username=prof_username)
#     group = Special_Students.objects.filter(professor=prof,pk=group_id).first()

#     if request.method == 'POST':
#         question_no = request.POST['question_no']
#         question = Question_DB.objects.filter(professor=prof,qno=question_no).first()
#         group.questions.add(question)

#     return render(request, 'prof/view_ques_in_group.html',{
#         'group': group, 'all_questions':Question_DB.objects.filter(professor=prof),
#         'questions_in_group': group.questions.all(), 'prof':prof
#     })


# def view_questionpaper_in_group(request,prof_username, group_id):
#     prof = User.objects.get(username=prof_username)
#     group = Special_Students.objects.filter(professor=prof,pk=group_id).first()

#     if request.method == 'POST':
#         qpaper_title = request.POST['qpaper_title']
#         qpaper = Question_Paper.objects.get(qPaperTitle = qpaper_title)
#         group.question_papers.add(qpaper)
    
#     return render(request, 'prof/view_qpaper_in_group.html',{
#         'group':group, 'all_qpapers': Question_Paper.objects.filter(professor=prof),
#         'qpapers_in_group': group.question_papers.all(),'prof':prof
#     })

def delete_group(request,prof_username, group_id):
    prof = User.objects.get(username=prof_username)
    Special_Students.objects.filter(professor=prof,pk=group_id).delete()
    
    return render(request, 'prof/addview_groups.html', {
        'special_students_db': Special_Students.objects.filter(professor=prof), 'prof':prof
    })

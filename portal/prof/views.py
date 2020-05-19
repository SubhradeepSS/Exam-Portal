from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Student

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
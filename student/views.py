from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def index(request, stud_username):
    student = User.objects.get(username=stud_username)
    return render(request, 'student/index.html',{
        'stud': student
    })

# def loginStud(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             return redirect("student:index")
#         else:
#             return redirect("student:loginStud")
    
#     return render(request,"student/login.html")

# def logoutStud(request):
#     logout(request)
#     return redirect('student:loginStud')
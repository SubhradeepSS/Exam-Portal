from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('student:loginStud')
    return render(request, 'student/index.html')

def loginStud(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("student:index")
        else:
            return redirect("student:loginStud")
    
    return render(request,"student/login.html")

def logoutStud(request):
    logout(request)
    return redirect('student:loginStud')
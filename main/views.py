from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if user.groups.filter(name='Professor').exists():
                return redirect('prof:index', prof_username=username)
            return redirect('student:index', stud_username=username)
        else:
            return render(request, 'main/login.html', {
                'wrong_cred_message': 'Error'
            })

    return render(request, 'main/login.html')

# def home(request, username):
#     user = User.objects.get(username=username)
#     return render(request, 'main/user_home.html',{
#         'user': user
#     })

def logoutUser(request):
    logout(request)
    return render(request, 'main/logout.html',{
        'logout_message': 'Logged out Successfully'
    })
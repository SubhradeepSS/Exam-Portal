from django.shortcuts import render
from django.contrib.auth.models import User

# separate views import
from .exam import *
from .group import *
from .question import *
from .question_paper import *
from .student import *

def index(request, prof_username):
    prof = User.objects.get(username=prof_username)
    return render(request, 'prof/index.html', {
        'prof': prof
    })

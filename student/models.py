from django.db import models
from main.models import *
from django.contrib.auth.models import User
# Create your models here.


class Stu_Question(Question_DB):
    professor = None
    student = models.ForeignKey(User, limit_choices_to={
        'groups__name': "Student"}, on_delete=models.CASCADE, null=True, blank=True)
    choice = models.CharField(max_length=3, default="E", null=True, blank=True)

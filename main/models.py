from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
# class Student(models.Model):
#     username = models.IntegerField()
#     password = models.CharField(max_length=500)

#     def __str__(self):
#         return f'{self.username}'

# class StudentForm(ModelForm):
#     class Meta:
#         model = Student
#         fields = '__all__'

class Question_DB(models.Model):
    #added question number for help in question paper
    professor = models.ForeignKey(User,limit_choices_to={'groups__name': "Professor"}, on_delete=models.CASCADE)
    qno = models.AutoField(primary_key=True)
    question = models.CharField(max_length=100)
    optionA = models.CharField(max_length=100)
    optionB = models.CharField(max_length=100)
    optionC = models.CharField(max_length=100)
    optionD = models.CharField(max_length=100)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return f'Question No.{self.qno}: {self.question} \t\t Options: \nA. {self.optionA} \nB.{self.optionB} \nC.{self.optionC} \nD.{self.optionD} '


class QForm(ModelForm):
    class Meta:
        model = Question_DB
        fields = '__all__'
        exclude = ['qno', 'professor']

        
class Question_Paper(models.Model):
    professor = models.ForeignKey(User,limit_choices_to={'groups__name': "Professor"}, on_delete=models.CASCADE)    
    qPaperTitle = models.CharField(max_length=100) 
    questions = models.ManyToManyField(Question_DB)
    
    def __str__(self):
        return f' Question Paper Title :- {self.qPaperTitle}\n'


class Special_Students(models.Model):
    professor = models.ForeignKey(User,limit_choices_to={'groups__name': "Professor"}, on_delete=models.CASCADE)
    students = models.ManyToManyField(User, limit_choices_to={'groups__name': "Student"}, related_name='students')
    # questions = models.ManyToManyField(Question_DB)
    category_name = models.CharField(max_length=10)
    # question_papers = models.ManyToManyField(Question_Paper)

    def __str__(self):
        return self.category_name


class Exam_Model(models.Model):
    professor = models.ForeignKey(User,limit_choices_to={'groups__name': "Professor"}, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    total_marks = models.IntegerField()
    duration = models.IntegerField()
    question_paper = models.ForeignKey(Question_Paper,on_delete=models.CASCADE)
    student_group = models.ManyToManyField(Special_Students)

    def __str__(self):
        return self.name

class ExamForm(ModelForm):
    class Meta:
        model = Exam_Model
        fields = '__all__'
        exclude = ['professor']
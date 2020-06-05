from django.db import models
from django.forms import ModelForm

# Create your models here.
class Student(models.Model):
    username = models.IntegerField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.username}'


# Added option in question. Changes made in html and views also
class Question_DB(models.Model):
    #added question number for help in question paper
    qno = models.AutoField(primary_key=True)
    number=models.IntegerField(default=1)
    question = models.CharField(max_length=100)
    optionA = models.CharField(max_length=100)
    optionB = models.CharField(max_length=100)
    optionC = models.CharField(max_length=100)
    optionD = models.CharField(max_length=100)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return f'Question No.{self.qno}: {self.question} \t\t Options: \nA. {self.optionA} \nB.{self.optionB} \nC.{self.optionC} \nD.{self.optionD} '

class QNO(models.Model):
    number=models.IntegerField(default=1)
    nid = models.AutoField(primary_key=True)
    def __str__(self):
        return f'{self.number}'
        
class Question_Paper(models.Model):
    
    qPaperTitle = models.CharField(max_length=100) 
    questions = models.ManyToManyField(Question_DB)
    
    def __str__(self):
        return f' Question Paper Title :- {self.qPaperTitle}\n'


class Special_Students(models.Model):
    students = models.ManyToManyField(Student)
    questions = models.ManyToManyField(Question_DB)
    category_name = models.CharField(max_length=10)
    question_papers = models.ManyToManyField(Question_Paper)

    def __str__(self):
        return self.category_name


class Exam_Model(models.Model):
    name = models.CharField(max_length=50)
    total_marks = models.IntegerField()
    duration = models.IntegerField()
    question_paper = models.ForeignKey(Question_Paper,on_delete=models.CASCADE)
    student_group = models.ForeignKey(Special_Students,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ExamForm(ModelForm):
    class Meta:
        model = Exam_Model
        fields = '__all__'
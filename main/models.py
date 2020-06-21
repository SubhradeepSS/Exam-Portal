from django.db import models
from django.forms import ModelForm, TextInput
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User
from django.conf import settings

class Question_DB(models.Model):
    # added question number for help in question paper
    professor = models.ForeignKey(User, limit_choices_to={
                                  'groups__name': "Professor"}, on_delete=models.CASCADE, null=True, blank=True)
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
    professor = models.ForeignKey(User, limit_choices_to={
                                  'groups__name': "Professor"}, on_delete=models.CASCADE)
    qPaperTitle = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question_DB)

    def __str__(self):
        return f' Question Paper Title :- {self.qPaperTitle}\n'


class Special_Students(models.Model):
    professor = models.ForeignKey(User, limit_choices_to={
                                  'groups__name': "Professor"}, on_delete=models.CASCADE)

    # questions = models.ManyToManyField(Question_DB)
    category_name = models.CharField(max_length=10)
    # question_papers = models.ManyToManyField(Question_Paper)

    students = models.ManyToManyField(
        User, limit_choices_to={'groups__name': "Student"}, related_name='students')

    def __str__(self):
        return self.category_name


class Group_Form(ModelForm):
    class Meta:
        model = Special_Students
        fields = '__all__'
        exclude = ['professor']


class Exam_Model(models.Model):
    professor = models.ForeignKey(User, limit_choices_to={
                                  'groups__name': "Professor"}, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    total_marks = models.IntegerField()
    duration = models.IntegerField()
    question_paper = models.ForeignKey(
        Question_Paper, on_delete=models.CASCADE, related_name='exam')
    student_group = models.ManyToManyField(Special_Students, related_name='exam')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name


class ExamForm(ModelForm):
    class Meta:
        model = Exam_Model
        fields = '__all__'
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'end_time': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }
        exclude = ['professor']

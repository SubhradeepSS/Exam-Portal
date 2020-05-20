from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.IntegerField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return f'Student: Username-{self.username} Password-{self.password}'

class Question_DB(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return f'Question: {self.question}, Answer: {self.answer}'

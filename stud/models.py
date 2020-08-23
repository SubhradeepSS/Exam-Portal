from django.db import models
from main.models import Question_DB, Question_Paper, Exam_Model

# Create your models here.
class StudQuestion(Question_DB):
    attempted_ans = models.CharField(max_length=200, default='E')
    parent = models.ForeignKey(Question_DB, on_delete=models.CASCADE)

class StudQuestion_Paper(Question_Paper):
    questions = models.ManyToManyField(StudQuestion)
    parent = models.ForeignKey(Question_Paper, on_delete=models.CASCADE)

class StudExam(Exam_Model):
    question_paper = models.ForeignKey(StudQuestion_Paper, on_delete=models.CASCADE, related_name='exam')
    attempt_starttime = models.DateTimeField()
    score = models.IntegerField(default=0)
    attempted = models.BooleanField(default=False)
    parent = models.ForeignKey(Exam_Model, on_delete=models.CASCADE)
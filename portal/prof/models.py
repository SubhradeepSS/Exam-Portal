from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.IntegerField()
    password = models.CharField(max_length=500)

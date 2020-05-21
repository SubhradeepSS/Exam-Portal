from django.contrib import admin
from .models import Student,Question_DB, Special_Students

# Register your models here.
admin.site.register(Student)
admin.site.register(Question_DB)
admin.site.register(Special_Students)
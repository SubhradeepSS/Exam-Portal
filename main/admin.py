from django.contrib import admin
from .models import Question_DB, Question_Paper, Special_Students
# Register your models here.
admin.site.register(Question_DB)
admin.site.register(Question_Paper)
admin.site.register(Special_Students)
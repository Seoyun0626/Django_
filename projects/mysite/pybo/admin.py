from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin) # admin 사이트에서 Question 모델 데이터 쉽게 사용 가능(장고 쉘에서 하던 작업)





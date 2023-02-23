from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200) # 제목 : 글자 수 제한O
    content = models.TextField() # 내용 : 글자 수 제한X
    create_date = models.DateTimeField() # 날짜, 시간 관련 속성

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 다른 모델과의 연결 + 질문 삭제하면 -> 답변 삭제해라
    content = models.TextField()
    create_date = models.DateTimeField()


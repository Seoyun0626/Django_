from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    subject = models.CharField(max_length=200) # 제목 : 글자 수 제한O
    content = models.TextField() # 내용 : 글자 수 제한X
    create_date = models.DateTimeField() # 날짜, 시간 관련 속성
    modify_date = models.DateTimeField(null=True, blank=True) # null=True : modify_date 열에 null 허용, blank=Ture : form.is_valie()를 통한 입력 폼 데이터 검사 시 값 없어도 됨
    author = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete : 계정이 삭제되면 계정과 연결된 Q모델 데이터 모두 삭제

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 다른 모델과의 연결 + 질문 삭제하면 -> 답변 삭제해라
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)


# Comment 구성요소 : 댓글(글쓴이, 내용, 작성일시, 수정일시, 이 댓글이 달린 질문, 이 댓글이 달린 답변)
# 질문에 댓글 작성 -> question필드 값 저장, 답변에 댓글 작성 -> answer필드 값 저장 => 둘 중 하나 필드 값 => null=True, blank=True
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True,
                                 on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)


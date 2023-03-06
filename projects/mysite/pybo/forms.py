from django import forms
from pybo.models import Question, Answer, Comment
from pybo.models import Question
# 아래 같은 클래스 : 장고 폼 (폼, 모델 폼)
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject','content']
        # subject, content 한글로 표시
        labels = {
            'subject' : '제목',
            'content' : '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '답변내용',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content' : '댓글내용',
        }
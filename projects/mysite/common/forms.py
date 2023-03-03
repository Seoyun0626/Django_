# 회원가입에 사용할 폼 만들기

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# UserCreationForm(사용자 이름, 비밀번호1, 비밀번호2)를 상속하고 email속성 추가
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")

from django.urls import path

from . import views

app_name='pybo' # URL별칭에서 중복문제 해결을위한 네임스페이스 과정

urlpatterns = [
    path('', views.index,name='index'), # config/urls.py에서 pybo/에 대해 처리 -> 빈 문자열 넘기기, /pybo/ = index
    path('<int:question_id>/', views.detail, name='detail'), # question_id에 값 저장된 후 views.detail 함수 실행, /pybo/2/ = detail
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]
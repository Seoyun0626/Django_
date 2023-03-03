from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'), # django.contib.auth 앱의 LoginView 클래스를 활용 -> views.py 파일 수정 필요 없음
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]

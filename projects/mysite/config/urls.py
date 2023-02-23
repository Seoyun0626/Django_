"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    htps://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')), # pybo 앱 관련 urls.py파일을 따로 구성, pybo/ 시작하는 페이지 요청 -> pybo/urls.py 참고
] # 호스트명, 포트는 환경에 따라 변화 + 장고가 이미 알고 있는 값 -> urlpatterns에 입력X

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm

def signup(request):
    '''
    회원가입
    '''
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #화면에서 입력한 값을 얻기 위해 사용하는 함수
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else: # GET요청
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})



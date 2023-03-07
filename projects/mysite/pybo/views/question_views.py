from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question

@login_required(login_url='common:login')
def question_create(request):
    '''
    pybo 질문 등록
    '''
    # 입력데이터 저장을 위한 코드
    if request.method == 'POST': # 저장하기 버튼을 누를 때
        form = QuestionForm(request.POST) # 화면에서 전달받은 데이터로 폼의 값 채우기
        if form.is_valid(): # form이 유요한지 검사
            question = form.save(commit=False) # commit=False는 임시 저장
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm() # request.method 가 GET인 경우 = 등록하기 버튼을 누를 때
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    '''
    질문 수정
    '''
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다') #messages 모듈은 오류를 임의로 발생시키고 싶은 경우 -> 넌필드 오류에 해당
        return redirect('pybo:detail', question_id=question.id)

    if request.method == "POST": # 저장버튼을 누를 때
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else: # 수정버튼을 누를 때
        form = QuestionForm(instance=question) #instance=question : GET 요청으로 질문 수정 화면 -> 기존에 저장되어 있던 제목, 내용 반영된 상태에서 수정가능하도록
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    '''
    pybo 질문 삭제
    '''
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')
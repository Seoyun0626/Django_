from django.shortcuts import render, get_object_or_404 , redirect # render : 템플릿 파일을 사용하여 화면에 출력할 수 있도록 하는 함수, redirect : 페이지 이동을 수행
from django.http import HttpResponse # HttpResponse : 페이지 요청에 대한 응답을 할 때 사용하는 클래스
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from .forms import QuestionForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request): # request : 장고에 의해 자동으로 전달되는 HTTP요청 객체, 사용자가 전달한 데이터 확인할 때 사용
    '''
    pybo 목록 출력
    '''
    # 입력인자
    page = request.GET.get('page', '1') #페이지 , GET 방식 요청 URL에서 page값을 가져올 때 사용

    # 조회
    question_list = Question.objects.order_by('-create_date') # order_by : 작성한 날짜의 역순으로 조회

    # 페이징 처리
    paginator = Paginator(question_list, 10) #페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list' : page_obj}
    return render(request, 'pybo/question_list.html', context) # context에 있는 question_list를 pybo/question_list.html 파일에 적용하여 HTML 코드로 변환


def detail(request, question_id):
    '''
    pybo 내용 출력
    '''
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)

# def answer_create(request, question_id): # request : textarea에 입력된 데이터
#     '''
#     pybo 답변 등록
#     '''
#     question = get_object_or_404(Question, pk=question_id)
#     question.answer_set.create(content=request.POST.get('content'),
#                                create_date=timezone.now()) # Question모델을 통해 Answer 모델 데이터 생성을 위해 위 함수 사용
#     return redirect('pybo:detail', question_id=question.id)

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


@login_required(login_url='common:login') #로그인이 되었는지 우선 검사 -> 로그아웃상태 -> @에 적용된 함수 호출 -> 로그인화면으로 이동
def answer_create(request, question_id):
    '''
    pybo 답변 등록
    '''
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question' : question, 'form' : form}
    return render(request, 'pybo/question_detail.html', context)
    context = {'form' : form}
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
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
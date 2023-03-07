from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question



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


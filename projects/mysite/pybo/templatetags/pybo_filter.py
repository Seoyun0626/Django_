import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter # 에너테이션 적용 -> 템플릿에서 필터로 사용 가능
def sub(value, arg):
    return value - arg # 기존값 - 입력값

@register.filter
def mark(value): # markdown모듈과 mark_safe함수를 이용하여 문자열을 HTML코드로 변환하여 반환 -> markdown문법에 맞는 HTMl생성
    extensions = ["nl2br", "fenced_code"] # 줄바꿈문자 ->br태그로 => enter한번 = 줄바꿈
    return mark_safe(markdown.markdown(value, extensions=extensions))
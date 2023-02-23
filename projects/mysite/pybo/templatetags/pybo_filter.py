from django import template

register = template.Library()


@register.filter # 에너테이션 적용 -> 템플릿에서 필터로 사용 가능
def sub(value, arg):
    return value - arg # 기존값 - 입력값
# author: 庸了个白
# contact: yejue@yjstudy1.com
# file: customize_test
# time: 2019/12/4
import datetime
from django import template

register = template.Library()


# 自定义过滤器
@register.filter
def add_star(value):
    return '*****'+str(value)+'*****'


@register.filter(name='add_star2')
def add_star2(value, num):
    return '{}{}{}'.format('*'*num, str(value), '*'*num)


@register.simple_tag
def current_time():
    return datetime.datetime.now()


@register.simple_tag
def current_time2(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.simple_tag(takes_context=True)
def get_other(context):
    return context.get('string')


# 包含标签
@register.inclusion_tag('test/include_tag_mode1.html')
def include_mode1():
    return {'content': [i for i in range(10)]}

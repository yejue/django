from django.shortcuts import render, redirect, reverse
from django.template.loader import get_template
from django.http import HttpResponse

# Create your views here.


def index(request, **kwargs):
    return HttpResponse('我是book的主页')


def test1(request, **kwargs):
    if kwargs.get('redirect') == 1:
        print('我跑路了')
        return redirect('ceshi2')
    return HttpResponse('跑路跳转之前的test1')


def test2(request, **kwargs):
    if kwargs.get('redirect') == 1:
        print('我接收到了跑路信息')
    return HttpResponse("我是test2")

# ————————————传入测试的东西 ——————————————#


class ClassTest(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        return '我是类的run'


def test():
    return "我是一个测试的函数"


list1 = ['a', 'b', 'c', 'd']
tu1 = ('a', 'b', 'c', 'd')
string1 = '我是一个测试的字符串'
dict1 = {
    'key1': '我是测试用的字典value'
}


# 使用render 渲染]
def index_mode(request, **kwargs):
    return render(request, 'book/book_index.html', context={
        'classTest': ClassTest('一个名字'),
        'test': test,
        'list1': list1,
        'tuple1': tu1,
        'string1': string1,
        'dict1': dict1
    })


# 硬编码页面渲染
def index_mode2(request, **kwargs):
    return HttpResponse('硬编码页面')


# 获取模板
def index_mode3(request, **kwargs):
    temp = get_template('book/book_index.html')
    html = temp.render()
    return HttpResponse(html)

# 模板的变量传递


from django.shortcuts import render, redirect, reverse
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

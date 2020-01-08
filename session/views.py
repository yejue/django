from django.shortcuts import render, redirect, reverse
from django.views import View
from django.http import HttpResponse
# Create your views here.


def home_page(request):
    username = request.session.get('username')
    return render(request, 'session/home.html', context={
        'username': username,
    })


class Login1(View):

    def get(self, request):
        print('视图函数开始执行')
        return render(request, 'session/login.html')

    def post(self, request):
        username = request.POST.get('username')
        request.session['username'] = username
        return redirect(reverse('home'))


class Login2(object):

    def __init__(self, request):
        self.request = request

    def render(self):
        print('视图函数开始执行')
        return render(self.request, 'session/login.html')


def index_test(request):
    obj = Login2(request)
    return obj

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from mydjango.settings import MEDIA_ROOT
import os
import uuid
import datetime


# Create your views here.


# def request_get_post(request):
#     if request.method == 'GET':
#         value = request.GET.get('value')
#         values = request.GET.getlist('value')
#         return render(request, 'request/request.html', context={
#             'value': value,
#             'values': values
#         })
#     elif request.method == 'POST':
#         value = request.POST.get('test')
#         values = request.POST.getlist('test')
#         return HttpResponse('The value is:{}, <br> The values are:{}'.format(value, values))
#
#
# class RequestGP(View):
#
#     def get(self, request):
#         value = request.GET.get('value')
#         values = request.GET.getlist('value')
#         return render(request, 'request/request.html', context={
#             'value': value,
#             'values': values
#         })
#
#     def post(self, request):
#         value = request.POST.get('test')
#         values = request.POST.getlist('test')
#         return HttpResponse('The value is:{}, <br> The values are:{}'.format(value, values))


def request_get_post(request):
    if request.method == 'GET':
        value = request.GET.get('value')
        values = request.GET.getlist('value')
        print(value)
        print(values)
        return render(request, 'request/request.html')
    elif request.method == 'POST':
        value = request.POST.get('test')
        values = request.POST.getlist('test')
        print(value)
        print(values)
        return HttpResponse('访问成功')


class RequestGP(View):

    def get(self, request):
        value = request.GET.get('value')
        values = request.GET.getlist('value')
        print(value)
        print(values)
        return render(request, 'request/request.html')

    def post(self, request):
        value = request.POST.get('test')
        values = request.POST.getlist('test')
        print(value)
        print(values)
        return HttpResponse('访问成功')


class Upload(View):

    def get(self, request):
        return render(request, 'request/upload.html')

    def post(self, request):
        file = request.FILES.get('upload')
        print(dir(file))
        print(type(file))
        path_name = self.named(file.name)
        with open('{}'.format(path_name), 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        return HttpResponse('上传完成')

    def named(self, filename):
        """
        输入一个原文件名
        生成包含文件存储路径的文件名
        :return: a string
        """
        ext = os.path.splitext(filename)[1]
        return os.path.join(MEDIA_ROOT, str(uuid.uuid4()) + ext)


def set_cookie(request):
    response = HttpResponse('测试')
    response.set_cookie('user', 'ylgb', max_age=30)     # 30秒后过期
    response.set_cookie('user', 'ylgb2', expires=datetime.datetime.now() + datetime.timedelta(days=1))  # 一天后过期
    return response


def get_cookie(request):
    cookie = request.COOKIES
    return HttpResponse(cookie.items())


def delete_cookie(request):
    response = HttpResponse('测试')
    response.delete_cookie('user')
    return response




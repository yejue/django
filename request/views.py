from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

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


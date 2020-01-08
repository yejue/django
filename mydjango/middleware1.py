# author: 庸了个白
# contact: yejue@yjstudy1.com
# file: middleware1
# time: 2020/1/7

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class TestMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print('这里是request预处理函数')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('这是 view 预处理函数')

    def process_template_response(self, request, response):
        print('调用了template')
        return response

    def process_exception(self, request, exception):
        print('调用了exception函数')
        return HttpResponse(exception)

    def process_response(self, request, response):
        print('response 后处理函数')
        return response

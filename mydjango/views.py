# author: 庸了个白
# contact: yejue@yjstudy1.com
# file: views
# time: 2019/11/7

from django.http import HttpResponse


def index(request):
    return HttpResponse('hello django')


def index2(request, name, sex):
    return HttpResponse('{}是最帅的{}'.format(name, sex))

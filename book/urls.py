# author: 庸了个白
# contact: yejue@yjstudy1.com
# file: urls
# time: 2019/11/8

from django.urls import path
from .views import index, test1, test2

urlpatterns = [
    path('index/', index),
    path('test1/', test1),
    path('test2/', test2, name='ceshi2'),
]

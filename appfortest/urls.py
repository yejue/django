# author: 庸了个白
# contact: yejue@yjstudy1.com
# file: urls
# time: 2019/11/28

from django.urls import path
from .views import test_mode, index, filter_content

urlpatterns = [
    path('testmode/', test_mode),
    path('index/', index),
    path('filter_content/', filter_content)
]

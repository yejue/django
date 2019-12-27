# author: 庸了个白
# contact: yejue@yjstudy1.com
# file: urls
# time: 2019/12/26

from django.urls import path
from .views import request_get_post, RequestGP, Upload

urlpatterns = [
    path('req/', request_get_post),
    path('req2/', RequestGP.as_view()),
    path('upload/', Upload.as_view(), name='upload')

]

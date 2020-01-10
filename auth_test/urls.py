# author: 庸了个白
# contact: yejue@yjstudy1.com
# file: urls
# time: 2020/1/10

from django.urls import path
from .views import index, Login, Register, delete, blog_list, Write, login_out, test1


urlpatterns = [
    path('index/', index, name='index'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('write/', Write.as_view(), name='write'),
    path('blogs/', blog_list, name='blog2'),
    path('delete/<blog_id>', delete, name='dele'),
    path('logout/', login_out, name='logout'),
    path('test1/', test1, name='test1'),
]


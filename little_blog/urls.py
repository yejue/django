# author: 庸了个白
# contact: yejue@yjstudy1.com
# file: urls
# time: 2019/12/25

from django.urls import path
from .views import index, blog_add, blog_detail, blog_list, delete, edit


urlpatterns =[
    path('index/', index),
    path('blog_add/', blog_add, name='blog_add'),
    path('blog_list/', blog_list, name='blog_list'),
    path('blog_detail/<blog_id>', blog_detail, name='blog_detail'),
    path('delete/<blog_id>', delete, name='delete'),
    path('edit/<blog_id>', edit, name='edit'),
]
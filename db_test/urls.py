# author: 庸了个白
# contact: yejue@yjstudy1.com
# file: urls
# time: 2019/12/10

from django.urls import path
from .views import add, select, update, delete, insert, relation_action

urlpatterns = [
    path('add/', add),
    path('select/', select),
    path('delete/', delete),
    path('update/', update),
    path('insert/', insert),
    path('relation_action/', relation_action),
]
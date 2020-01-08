# author: 庸了个白
# contact: yejue@yjstudy1.com
# file: urls
# time: 2019/12/31

from django.urls import path
from .views import home_page, Login1, index_test


urlpatterns = [
    path('home/', home_page, name='home'),
    path('login/', Login1.as_view(), name='login'),
    path('index/', index_test, name='login2')
]

# author: 庸了个白
# contact: yejue@yjstudy1.com
# file: urls
# time: 2019/12/31

from django.urls import path
from .views import home_page, Login


urlpatterns = [
    path('home/', home_page, name='home'),
    path('login/', Login.as_view(), name='login'),
]

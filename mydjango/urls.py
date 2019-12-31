"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from .views import index, index2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    # path('index2/<name>&<sex>', index2),
    # path('index2/name=<name>&sex=<sex>', index2)
    # path支持的默认转换器
    # path('index2/name=<int:name>&sex=<sex>', index2)
    re_path(r'^index2/(?P<name>[a-z]+)&(?P<sex>[0-9]+)', index2),
    path('book/', include('book.urls'), {'redirect': 1}),
    path('appfortest/', include('appfortest.urls')),
    path('db_test/', include('db_test.urls')),
    path('little_blog/', include('little_blog.urls')),
    path('request/', include('request.urls')),
    path('session/', include('session.urls')),
]

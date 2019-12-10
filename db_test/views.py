from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import User


def add(request):
    # 方法一
    temp = User(name='小明', city='珠海')
    temp.save()
    # 方法二
    temp2 = User()
    temp2.name = '小红'
    temp2.city = '广州'
    temp2.save()
    # 方法三
    User.objects.create(name='小亮', city='珠海')
    # 方法四
    User.objects.get_or_create(name='小李', city='重庆')
    return HttpResponse('添加成功')


def delete(request):
    User.objects.filter(city='珠海').delete()
    return HttpResponse('删除完成')


def select(request):
    # # 查询所有
    # rs = User.objects.all()
    # 查询单个对象
    rs = User.objects.get(id=1)
    # 查询满足条件的对象
    # rs = User.objects.filter(name='小明')
    return render(request, 'db_test/add_del_select_update.html', context={
        'rs': rs
    })


def update(request):
    # # 方法一
    # rs = User.objects.get(id=1)
    # rs.name = '小红'
    # rs.save()
    # 方法二
    # User.objects.filter(name='小明').update(city='香港')
    # 方法三
    User.objects.all().update(city='珠海')

    return HttpResponse('修改成功')

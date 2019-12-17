from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
from .models import User


def add(request):
    # # 方法一
    # temp = User(name='小明', city='珠海')
    # temp.save()
    # # 方法二
    # temp2 = User()
    # temp2.name = '小红'
    # temp2.city = '广州'
    # temp2.save()
    # # 方法三
    User.objects.create(name='yejue', city='珠海')
    User.objects.create(name='YEJUE', city='珠海')
    # # 方法四
    # User.objects.get_or_create(name='小李', city='重庆')
    return HttpResponse('添加成功')


def delete(request):
    User.objects.filter(city='珠海').delete()
    return HttpResponse('删除完成')


def select(request):
    # # 查询所有
    # rs = User.objects.all()
    # 查询单个对象
    # rs = User.objects.get(id=1)
    # 查询满足条件的对象
    # rs = User.objects.filter(name='小明')
    # 查询第一条数据
    rs = User.objects.first()
    # 查询最后一条数据
    rs = User.objects.last()
    # 排除查询，查询不满足条件的数据
    rs = User.objects.exclude(name='小红')
    # 查询排序
    rs = User.objects.order_by('-id')
    # 查询结果数据转化为字典
    rs = User.objects.all().values()
    # 查询结果计数
    rs = User.objects.all().count()
    # 条件查询
    # exact 和 iexact
    rs = User.objects.filter(name__exact='yejue')
    rs = User.objects.filter(name__iexact='yejue')
    # 以...开头，以...结尾
    rs = User.objects.filter(name__startswith='小')
    rs = User.objects.filter(name__endswith='明')
    # 成员所属,in 查询
    rs = User.objects.filter(name__in=['小明', '小红'])
    # range 数字区间查询
    rs = User.objects.filter(id__range=(12, 17))
    # 大于 > ，大于等于 >= , 小于<， 小于等于 <=
    rs = User.objects.filter(id__lt=15)   # 小于15
    rs = User.objects.filter(id__lte=15)   # 小于等于15
    rs = User.objects.filter(id__gt=15)   # 大于15
    rs = User.objects.filter(id__gte=15)   # 大于等于15
    # 使用or条件查询
    rs = User.objects.filter(Q(name='小明') | Q(id=15))
    print(rs.query)
    #
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

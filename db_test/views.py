from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
from .models import User, College, Student, Course, StudentDetail


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
    Student.objects.filter(s_id='201907').delete()
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


# 插入数据
def insert(request):
    # 学院表
    # College.objects.get_or_create(college_name='计算机')
    # College.objects.get_or_create(college_name='经济管理')
    # College.objects.get_or_create(college_name='土木工程')
    # College.objects.get_or_create(college_name='数学')

    # 学生表
    # Student.objects.get_or_create(s_id=201901, student_name='小叶', c_id_id=1)
    # Student.objects.get_or_create(s_id=201902, student_name='小黄', c_id_id=2)
    # Student.objects.get_or_create(s_id=201903, student_name='小嘉', c_id_id=2)
    # Student.objects.get_or_create(s_id=201904, student_name='小琳', c_id_id=3)
    # Student.objects.get_or_create(s_id=201905, student_name='小巧', c_id_id=3)
    # Student.objects.get_or_create(s_id=201906, student_name='小伏', c_id_id=4)

    # 学生详情表
    # StudentDetail.objects.get_or_create(student_age=12, student_phone=186612345, student_id=201901)
    # StudentDetail.objects.get_or_create(student_age=13, student_phone=186634674, student_id=201902)
    # StudentDetail.objects.get_or_create(student_age=11, student_phone=186634655, student_id=201903)
    # StudentDetail.objects.get_or_create(student_age=15, student_phone=186633463, student_id=201904)
    # StudentDetail.objects.get_or_create(student_age=12, student_phone=186634421, student_id=201905)
    # StudentDetail.objects.get_or_create(student_age=14, student_phone=186634678, student_id=201906)

    # 课程表
    # Course.objects.get_or_create(course_name='python')
    # Course.objects.get_or_create(course_name='经济学')
    # Course.objects.get_or_create(course_name='土木工程制图')
    # Course.objects.get_or_create(course_name='应用数学')
    # Course.objects.get_or_create(course_name='毛概')
    # Course.objects.get_or_create(course_name='大英')

    return HttpResponse('执行完成')


# 关系表数据操作
def relation_action(request):
    c1 = College.objects.get(c_id=1)        # 一个学院的实例
    s2 = Student.objects.get(s_id=201901)   # 一个学生的实例
    # c1.student_set.add(s2)                  # 使用add为从表添加或修改外键值

    # 主表使用create为从表添加记录
    # c1.student_set.create(s_id=201907, student_name='小明')
    # c1.college.create(s_id=201908, student_name='cese')

    # 正向查询 从表查主表
    print(s2.c_id.college_name)
    print(s2.c_id.c_id)     # C_id 为外键名，详情可在上一章查看我的详细表结构
    # 反向查询 主表查从表
    print(c1.student_set.all())    # 查询与c1对应的所有记录
    print(c1.student_set.filter(s_id=201901))    # 查询与c1对应的指定记录
    # print(s2.college.college_name)

    # 删除
    # c1.student_set.remove()     # 指定删除
    # c1.student_set.clear()      # 清空

    # 一对一操作
    stu_detail = StudentDetail.objects.get(student_id=201901)
    stu1 = Student.objects.get(s_id=201901)

    # 正向查询
    print(stu_detail.student.student_name)
    # 反向查询
    print(stu1.studentdetail.student_phone)
    print(stu1.studentdetail.student_age)

    # 多对多操作

    # 六门课程实例
    co1 = Course.objects.get(co_id=1)
    co2 = Course.objects.get(co_id=2)
    co3 = Course.objects.get(co_id=3)
    co4 = Course.objects.get(co_id=4)
    co5 = Course.objects.get(co_id=5)
    co6 = Course.objects.get(co_id=6)

    # 六个学生实例
    s1 = Student.objects.get(s_id=201901)
    s2 = Student.objects.get(s_id=201902)
    s3 = Student.objects.get(s_id=201903)
    s4 = Student.objects.get(s_id=201904)
    s5 = Student.objects.get(s_id=201905)
    s6 = Student.objects.get(s_id=201906)

    # # 从学生表添加课程
    # s1.course_set.add(co1)
    # s1.course_set.add(co2)
    # s2.course_set.add(co3, co4)
    # s3.course_set.add(co4, co1)
    # # 从课程表添加学生
    # co2.student.add(s4, s5, s6)

    # 查询
    print(s1.course_set.all())                  # 查询学生s1报名的所有课程
    print(co1.student.all())                    # 查询课程co1报名的所有学生
    print(s1.course_set.filter(co_id__lt=3))    # 查询学生s1学习的所有co_id小于3的课程
    print(s3.course_set.filter(co_id__gt=3))    # 查询学生s3学习的所有co_id大于3的课程

    # 删除
    # s1.course_set.remove(co1)    # 移除课程co1
    # s1.course_set.clear()        # 清空学生s1的所有课程
    # co3.student.clear()          # 清空学习课程co3的所有学生

    # 多表联查
    # 查询包含小叶的学院
    rs = College.objects.filter(student__student_name='小叶')
    # 查询计算机学院学号名字以叶结尾的学生详情信息
    rs = StudentDetail.objects.filter(student__student_name__endswith='叶', student__c_id__college_name='计算机')
    # 查询土木工程学院学号大于201901的所有学生所报名的课程信息
    rs = Course.objects.filter(student__s_id__gt=201901, student__c_id__college_name='土木工程')

    print(rs)

    return render(request, 'db_test/add_del_select_update.html', context={
        'rs': rs
    })

from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=10, null=True)

    def __str__(self):
        return 'id : {}, name: {}, city: {}'.format(self.id, self.name, self.city)


# 学院表
class College(models.Model):
    c_id = models.AutoField(primary_key=True)
    college_name = models.CharField(max_length=30)

    def __str__(self):
        return "c_id={},college_name={}".format(self.c_id, self.college_name)


# 学生表
class Student(models.Model):
    s_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=20)
    c_id = models.ForeignKey(College, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "s_id={},student_name={}".format(self.s_id, self.student_name)


# 学生详情表
class StudentDetail(models.Model):
    sd_id = models.AutoField(primary_key=True)
    student_age = models.IntegerField()
    student_phone = models.IntegerField()
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    def __str__(self):
        return "sd_id={},student_age={},student_phone={}".format(self.sd_id, self.student_age, self.student_phone)


# 课程表
class Course(models.Model):
    co_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=30)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return "co_id={}, course_name={}".format(self.co_id, self.course_name)

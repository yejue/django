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


# 学生表
class Student(models.Model):
    s_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=20)
    c_id = models.ForeignKey(College, on_delete=models.CASCADE)


# 学生详情表
class StudentDetail(models.Model):
    sd_id = models.AutoField(primary_key=True)
    student_age = models.IntegerField()
    student_phone = models.IntegerField()
    student = models.OneToOneField(Student, on_delete=models.CASCADE)


# 课程表
class Course(models.Model):
    co_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=30)
    student = models.ManyToManyField(Student)

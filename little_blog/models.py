from django.db import models

# Create your models here.


# 博客表
class Blog(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_content = models.TextField()

    def __str__(self):
        return 'blog_title:{}'.format(self.blog_title)

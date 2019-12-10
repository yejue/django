from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=10, null=True)

    def __str__(self):
        return 'id : {}, name: {}, city: {}'.format(self.id, self.name, self.city)


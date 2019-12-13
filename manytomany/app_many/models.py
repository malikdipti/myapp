from django.db import models

class Publisher(models.Model):
    pid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    aid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    publisher_name=models.ManyToManyField(Publisher)



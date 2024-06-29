from django.db import models

# Create your models here.


class Market(models.Model):
    money = models.CharField(max_length=100)
    client = models.IntegerField()

class Client(models.Model):
    money = models.CharField(max_length=100)
    product = models.IntegerField()

class Worker(models.Model):
    pay = models.CharField(max_length=100)
    hours = models.IntegerField()
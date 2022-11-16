from django.db import models

class Product(models.Model):
    name = models.TextField(max_length=200)
    code = models.IntegerField(default=0)
    price = models.FloatField(default=0)

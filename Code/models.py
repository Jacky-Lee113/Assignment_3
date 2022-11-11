# MyApp/models.py

from django.db import models


class Product(models.Model):
    name = models.TextField()
    codes = models.IntegerField(min_value=1, max_value=5)
    price = models.IntegerField(min_value=0.00, max_value=50.00)
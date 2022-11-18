from django.db import models

class Product(models.Model):
    name = models.TextField(max_length=200)
    code = models.IntegerField(default=0)
    price = models.FloatField(default=0)

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def total():
        cart_total = 0
        for item in Cart.objects.all():
            cart_total += item.product.price * item.quantity

        return cart_total

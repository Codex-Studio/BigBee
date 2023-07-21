from django.db import models

from apps.products.models import Product

# Create your models here.
class Cart(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    items = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"{self.session_key}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cart}"
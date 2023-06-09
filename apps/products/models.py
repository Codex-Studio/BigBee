from django.db import models
from django.contrib.auth import get_user_model

from apps.categories.models import Category

User = get_user_model()

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_products",
        verbose_name="Пользователь"
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        related_name="category_products",
        verbose_name="Категория",
        null=True
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to='product_images/',
        verbose_name="Фотография",
        blank=True, null=True
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена"
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name="product_images",
        verbose_name="Продукт"
    )
    image = models.ImageField(
        upload_to="product_images/",
        verbose_name="Фотография"
    )

    def __str__(self):
        return f"{self.product}"
    
    class Meta:
        verbose_name = "Фотография продукта"
        verbose_name_plural = "Фотографии продуктов"
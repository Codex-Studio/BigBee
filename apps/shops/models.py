from django.db import models

from apps.categories.models import Category

# Create your models here.
class Shop(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название магазина"
    )
    description = models.TextField(
        verbose_name="Описание магазина",
        blank=True, null=True
    )
    logo = models.ImageField(
        upload_to="shop_images/",
        verbose_name="Логотип магазина"
    )
    banner = models.ImageField(
        upload_to="shop_banners/",
        verbose_name="Баннер магазина",
        blank=True, null=True
    )
    domain = models.URLField(
        max_length=200,
        verbose_name="Ссылка на магазин",
        blank=True, null=True
    )
    slug = models.SlugField(
        verbose_name="Slug"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name="category_shops",
        verbose_name="Категория магазина"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата регистрации магазина"
    )

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
import uuid

from apps.products.models import Product
from apps.shops.models import Shop

User = get_user_model()

# Create your models here.
class Billing(models.Model):
    class BillingReceiptTypeChoices(models.TextChoices):
        PICKUP = 'Pickup', _('Самовывоз')
        DELIVERY = 'Delivery', _('Доставка')
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        related_name="billing_user",
        verbose_name="Пользователь",
        blank=True, null=True
    )
    products = models.ManyToManyField(
        Product, related_name="billing_products",
        verbose_name="Товары"
    )
    shops = models.ManyToManyField(
        Shop, related_name="billing_shops",
        verbose_name="Магазины"
    )
    billing_receipt_type = models.CharField(
        max_length=100, choices=BillingReceiptTypeChoices.choices,
        default=BillingReceiptTypeChoices.DELIVERY,
        verbose_name=_('Вид получения товара')
    )
    payment_code = models.CharField(
        max_length=20, unique=True,
        verbose_name="Код оплаты биллинга",
    )
    status = models.BooleanField(
        default=False, verbose_name="Статус заказа"
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания биллинга"
    )

    def __str__(self):
        return f"{self.billing_receipt_type} {self.payment_code}"
    
    def save(self, *args, **kwargs):
        if not self.payment_code:
            self.payment_code = str(uuid.uuid4().int)[:20]  # Генерируем UUID и оставляем только первые 20 цифр
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Биллинг"
        verbose_name_plural = "Биллинги"
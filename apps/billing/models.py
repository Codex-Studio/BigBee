from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from apps.products.models import Product

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
    billing_receipt_type = models.CharField(
        max_length=100, choices=BillingReceiptTypeChoices.choices,
        default=BillingReceiptTypeChoices.DELIVERY,
        verbose_name=_('Вид получения товара')
    )
    status = models.BooleanField(
        default=False, verbose_name="Статус заказа"
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания биллинга"
    )

    def __str__(self):
        return f"{self.user} {self.created}"
    
    class Meta:
        verbose_name = "Биллинг"
        verbose_name_plural = "Биллинги"
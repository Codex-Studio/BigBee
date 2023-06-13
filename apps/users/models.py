from django.db import models
from django.contrib.auth.models import AbstractUser
import random, string

# Create your models here.
class User(AbstractUser):
    USER_ROLE_CHOICE = (
        ('Client', 'Client'),
        ('Partner', 'Partner')
    )
    user_role = models.CharField(
        max_length=100,
        choices=USER_ROLE_CHOICE,
        verbose_name="Роль пользователя",
        default='Client'
    )
    phone = models.CharField(
        max_length=50,
        verbose_name="Телефонный номер"
    )
    address = models.CharField(
        max_length=100,
        verbose_name="Адрес"
    )
    promo_code = models.CharField(
        max_length=100,
        blank=True, null=True
    )
    
    def __str__(self):
        return self.username 
    
    def save(self, *args, **kwargs):
        if not self.promo_code:
            self.promo_code = self.generate_promo_code()
        return super().save(*args, **kwargs)

    @staticmethod
    def generate_promo_code():
        characters = string.ascii_letters + string.digits
        code = ''.join(random.choice(characters) for _ in range(6)).upper()
        return code

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class Partnership(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='users_partnership',
        verbose_name="Пользователь",
        blank=True, null=True
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время заявки"
    )

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = "Заявка на партнерство"
        verbose_name_plural = "Заявка на партнерство"
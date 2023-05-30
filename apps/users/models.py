from django.db import models
from django.contrib.auth.models import AbstractUser

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
    promo_code = models.CharField(
        max_length=100,
        blank=True, null=True
    )
    
    def __str__(self):
        return self.username 
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        max_length=300,
        verbose_name="Описание"
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name="Логотип"
    )
    phone = models.CharField(
        max_length=100,
        verbose_name="Телефонный номер"
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"
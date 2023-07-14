# Generated by Django 4.2.1 on 2023-07-13 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название магазина')),
                ('description', models.TextField(verbose_name='Описание магазина')),
                ('logo', models.ImageField(upload_to='shop_images/', verbose_name='Логотип магазина')),
                ('banner', models.ImageField(upload_to='shop_banners/', verbose_name='Баннер магазина')),
                ('domain', models.URLField(verbose_name='Ссылка на магазин')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации магазина')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_shops', to='categories.category', verbose_name='Категория магазина')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
            },
        ),
    ]

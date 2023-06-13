# Generated by Django 4.2.1 on 2023-06-13 12:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_partnership'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnership',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Время заявки'),
            preserve_default=False,
        ),
    ]

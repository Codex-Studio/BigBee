from django.contrib import admin

from apps.shops.models import Shop

# Register your models here.
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'domain', 'category', 'created')
    search_fields = ('name', 'description', 'domain', 'category__title')
    prepopulated_fields = {'slug' : ('name', )}
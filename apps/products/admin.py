from django.contrib import admin

from apps.products.models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'category')
    search_fields = ('user__username', 'title')
    list_per_page = 20
from django.contrib import admin

from apps.products.models import Product, ProductImage

# Register your models here.
class ImageTabularInline(admin.TabularInline):
    model = ProductImage
    extra = 3

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('shop', 'title', 'category', 'created')
    search_fields = ('shop__name', 'title', 'created')
    list_per_page = 20
    inlines = [ImageTabularInline]

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
    list_per_page = 20
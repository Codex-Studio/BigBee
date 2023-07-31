from django.contrib import admin

from apps.products.models import Product, ProductImage, ProductFavorite

# Register your models here.
class ImageTabularInline(admin.TabularInline):
    model = ProductImage
    extra = 3

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('shop', 'title', 'category', 'created')
    search_fields = ('shop__name', 'title', 'created')
    fields = ('category', 'title', 'description', 'image', 'price')
    list_per_page = 20
    inlines = [ImageTabularInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_staff and request.user.shop:
            # Если пользователь является персоналом сайта (is_staff = True)
            # и у него есть магазин, показываем только товары, связанные с его магазином
            qs = qs.filter(shop=request.user.shop)
        return qs
    
    def save_model(self, request, obj, form, change):
        # Если поле shop не установлено (например, при создании нового товара),
        # устанавливаем его на магазин, связанный с текущим пользователем
        obj.shop = request.user.shop
        super().save_model(request, obj, form, change)

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
    list_per_page = 20

@admin.register(ProductFavorite)
class ProductFavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    search_fields = ('user__username', 'product__title')
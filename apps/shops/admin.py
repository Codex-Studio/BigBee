from django.contrib import admin

from apps.shops.models import Shop

# Register your models here.
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'domain', 'category', 'created')
    search_fields = ('name', 'description', 'domain', 'category__title')
    prepopulated_fields = {'slug' : ('name', )}

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_staff:
            # Если пользователь является персоналом сайта (is_staff = True),
            # показываем только данные, связанные с его магазином
            if request.user.shop:
                qs = qs.filter(name=request.user.shop)
        return qs
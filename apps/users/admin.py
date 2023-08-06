from django.contrib import admin

from apps.users.models import User, Partnership

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'date_joined')
    list_filter = ('username', )
    search_fields = ('username', 'first_name', 'last_name', 'email', 'date_joined')
    list_per_page = 20

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_staff and request.user.username and not request.user.is_superuser:
            # Если пользователь является персоналом сайта (is_staff = True)
            # и у него есть магазин, показываем только товары, связанные с его магазином
            qs = qs.filter(username=request.user.username)
        return qs

    def save_model(self, request, obj, form, change):
        # Если пароль не хэширован, установите новый случайный пароль и хешируйте его перед сохранением
        if not obj.password.startswith('pbkdf2_'):
            obj.set_password(User.objects.make_random_password())
        super().save_model(request, obj, form, change)

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        exclude_is_staff = ('password', 'is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions', 'promo_code')
        if not request.user.is_superuser:
            fields = [field for field in fields if field not in exclude_is_staff]
        return fields

    def get_readonly_fields(self, request, obj=None):
        if obj and not request.user.is_superuser and obj.is_staff:
            return ('date_joined', 'shop', 'user_role', 'last_login')  # Список полей, которые нужно сделать только для чтения
        return super().get_readonly_fields(request, obj)

@admin.register(Partnership)
class PartnershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'phone', 'created')
    list_filter = ('user', )
    search_fields = ('user__username', 'name', 'email', 'phone', 'created')
    list_per_page = 20
    ordering = ('-created', )
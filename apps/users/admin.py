from django.contrib import admin

from apps.users.models import User, Partnership

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'date_joined')
    list_filter = ('username', )
    search_fields = ('username', 'first_name', 'last_name', 'email', 'date_joined')
    list_per_page = 20

    def save_model(self, request, obj, form, change):
        # Если пароль не хэширован, установите новый случайный пароль и хешируйте его перед сохранением
        if not obj.password.startswith('pbkdf2_'):
            obj.set_password(User.objects.make_random_password())
        super().save_model(request, obj, form, change)

@admin.register(Partnership)
class PartnershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'phone', 'created')
    list_filter = ('user', )
    search_fields = ('user__username', 'name', 'email', 'phone', 'created')
    list_per_page = 20
    ordering = ('-created', )
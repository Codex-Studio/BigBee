from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from apps.settings.models import Setting

# Register your models here.
@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'logo')

    def get_queryset(self, request):
        # В этом методе вы можете переопределить queryset, чтобы отобразить только определенные данные для пользователя
        queryset = super().get_queryset(request)
        user = request.user
        if user.is_superuser:
            # Если пользователь суперпользователь, показываем все данные
            return queryset
        else:
            # Иначе, показываем только данные для этого пользователя
            return queryset.filter(user=user)
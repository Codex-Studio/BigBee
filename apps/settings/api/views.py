from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.settings.models import Setting
from apps.settings.api.serializers import SettingSerializer


class SettingAPIView(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
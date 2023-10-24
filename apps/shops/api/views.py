from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.shops.models import Shop
from apps.shops.api.serializers import ShopSerilizer

class ShopAPIView(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin):
    queryset = Shop.objects.all()
    serializer_class = ShopSerilizer
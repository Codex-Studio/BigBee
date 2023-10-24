from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.products.models import Product
from apps.products.api.serializers import ProductSerializer


class ProductAPIView(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
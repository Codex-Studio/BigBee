from rest_framework import serializers

from apps.shops.models import Shop


class ShopSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"
from django.urls import path

from apps.shops.views import shop_detail


urlpatterns = [
    path('<str:slug>/', shop_detail, name='shop_detail')
]
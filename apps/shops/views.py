from django.shortcuts import render

from apps.settings.models import Setting
from apps.products.models import Product
from apps.shops.models import Shop

# Create your views here.
def shop_detail(request, slug):
    setting = Setting.objects.latest('id')
    shop = Shop.objects.get(slug=slug)
    products = Product.objects.filter(shop=shop.id)
    return render(request, 'shops/detail.html', locals())
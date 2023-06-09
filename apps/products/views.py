from django.shortcuts import render

from apps.settings.models import Setting
from apps.products.models import Product

# Create your views here.
def product_detail(request, id):
    setting = Setting.objects.latest('id')
    product = Product.objects.get(id = id)
    related_products = Product.objects.filter(category=product.category)
    return render(request, 'products/detail.html', locals())
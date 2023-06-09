from django.shortcuts import render

from apps.settings.models import Setting
from apps.categories.models import Category
from apps.products.models import Product

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    categories = Category.objects.all()
    products = Product.objects.all()
    random_product = Product.objects.all().order_by('?')[:3]
    like_products = Product.objects.all().order_by('?')
    return render(request, 'index-2.html', locals())
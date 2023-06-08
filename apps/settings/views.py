from django.shortcuts import render

from apps.settings.models import Setting
from apps.categories.models import Category
from apps.products.models import Product

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    return render(request, 'index-2.html', locals())
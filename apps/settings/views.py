from django.shortcuts import render
from django.db.models import Sum, F, ExpressionWrapper, DecimalField, Q

from apps.settings.models import Setting
from apps.categories.models import Category
from apps.products.models import Product
from apps.carts.models import Cart, CartItem
from apps.shops.models import Shop

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    categories = Category.objects.all()
    random_categories = Category.objects.all().order_by('?')[:3]
    products = Product.objects.all()
    random_product = Product.objects.all().order_by('?')[:3]
    like_products = Product.objects.all().order_by('?')
    session_key = request.session.session_key
    cart = Cart.objects.filter(session_key=session_key).first()
    cart_items = []
    # Проверяем, что корзина существует перед использованием aggregate
    if cart:
        cart_items = CartItem.objects.filter(cart=cart).annotate(
            total_price=ExpressionWrapper(F('product__price') * F('quantity'), output_field=DecimalField())
        )

        total_price = cart_items.aggregate(total=Sum('total_price'))['total'] or 0
    else:
        cart_items = []
        total_price = 0
    return render(request, 'index.html', locals())

def about(request):
    setting = Setting.objects.latest('id')
    return render(request, 'home/about.html', locals())

def search(request):
    query = request.POST.get('query', '')
    results = []
    print(query)
    if query:
        # Используйте Q-объекты для выполнения поиска в моделях Shop и Product
        shop_results = Shop.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        product_results = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

        # Добавьте результаты поиска в список результатов
        results.extend(shop_results)
        results.extend(product_results)

    return render(request, 'search_results.html', {'results': results, 'query': query})
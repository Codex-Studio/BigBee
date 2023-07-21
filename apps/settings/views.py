from django.shortcuts import render
from django.db.models import Sum, F, ExpressionWrapper, DecimalField

from apps.settings.models import Setting
from apps.categories.models import Category
from apps.products.models import Product
from apps.carts.models import Cart, CartItem

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    categories = Category.objects.all()
    products = Product.objects.all()
    random_product = Product.objects.all().order_by('?')[:3]
    like_products = Product.objects.all().order_by('?')
    session_key = request.session.session_key
    cart = Cart.objects.filter(session_key=session_key).first()
    cart_items = []
    if cart:
        cart_items = CartItem.objects.filter(cart=cart).annotate(
            total_price=ExpressionWrapper(F('product__price') * F('quantity'), output_field=DecimalField())
        )
    total_price = cart_items.aggregate(total=Sum('total_price'))['total'] or 0
    return render(request, 'index-2.html', locals())
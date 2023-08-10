from django.shortcuts import render, redirect
from django.db.models import F, ExpressionWrapper, DecimalField, Sum
import asyncio

from apps.products.models import Product
from apps.carts.models import Cart, CartItem
from apps.carts.forms import AddToCartForm
from apps.settings.models import Setting
from apps.billing.forms import BillingForm
from apps.telegram.views import send_billing_notification
from apps.users.models import User

# Create your views here.
def add_to_cart(request):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']
            product = Product.objects.get(id=product_id)

            # Получаем или создаем корзину для текущей сессии
            session_key = request.session.session_key
            if not session_key:
                request.session.save()
                session_key = request.session.session_key

            cart, _ = Cart.objects.get_or_create(session_key=session_key)

            # Получаем объект CartItem по cart и product
            cart_item = CartItem.objects.filter(cart=cart, product=product).first()

            # Если CartItem существует, обновляем его количество, иначе создаем новый объект
            if cart_item:
                cart_item.quantity += quantity
                cart_item.save()
            else:
                cart_item = CartItem.objects.create(cart=cart, product=product, quantity=quantity)

    return redirect('cart')

def cart(request):
    setting = Setting.objects.latest('id')
    session_key = request.session.session_key
    cart = Cart.objects.filter(session_key=session_key).first()
    cart_items = []
    if cart:
        cart_items = CartItem.objects.filter(cart=cart).annotate(
            total_price=ExpressionWrapper(F('product__price') * F('quantity'), output_field=DecimalField())
        )
        total_price = cart_items.aggregate(total=Sum('total_price'))['total'] or 0
    else:
        cart_items = []
        total_price = 0
        
    if request.method == 'POST':
            form = BillingForm(request.POST)
            if form.is_valid():
                billing = form.save(commit=False)
                billing.user = request.user
                billing.save()

                # Получаем или создаем корзину для текущей сессии
                session_key = request.session.session_key
                if not session_key:
                    request.session.save()
                    session_key = request.session.session_key

                cart, _ = Cart.objects.get_or_create(session_key=session_key)

                # Получаем связанных менеджеров и отправляем им уведомления
                for cart_item in cart.items.all():
                    billing.products.add(cart_item)
                    billing.shops.add(cart_item.shop)
                    shop_id = cart_item.shop.id

                    # Получаем пользователей (менеджеров), связанных с магазином
                    users_in_shop = User.objects.filter(shop_id=shop_id)

                    for user in users_in_shop:
                        if user.telegram_chat_id:
                            asyncio.run(send_billing_notification(
                                manager_id=user.telegram_chat_id,
                                shop=cart_item.shop.name,
                                user=request.user.username,
                                products=", ".join([str(item) for item in billing.products.all()]),
                                billing_receipt_type=billing.billing_receipt_type,
                                payment_code=billing.payment_code,
                                created=billing.created.strftime("%Y-%m-%d %H:%M:%S")
                            ))
                            print("WORK")
                # Удаляем связи товаров с корзиной, не удаляя товары самих из базы данных
                cart.items.clear()

                return redirect('billing_success')
    else:
        form = BillingForm()
    return render(request, 'cart/index.html', locals())

def clear_cart(request):
    session_key = request.session.session_key
    if session_key:
        CartItem.objects.filter(cart__session_key=session_key).delete()

    return redirect('cart')

def remove_from_cart(request, product_id):
    session_key = request.session.session_key
    if session_key:
        CartItem.objects.filter(cart__session_key=session_key, product__id=product_id).delete()

    return redirect('cart')
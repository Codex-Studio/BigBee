from django.shortcuts import render, redirect

from apps.billing.models import Billing
from apps.billing.forms import BillingForm
from apps.products.models import Product
from apps.carts.models import Cart, CartItem

# Create your views here.
def create_billing(request):
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

            # Создаем связи между биллингом и товарами из корзины
            for cart_item in cart.items.all():
                print(cart_item)
                billing.products.add(cart_item)
                print(billing)
            
            # Удаляем связи товаров с корзиной, не удаляя товары самих из базы данных
            print(cart)
            cart.items.clear()

            return redirect('billing_success')
    else:
        form = BillingForm()

    return render(request, 'billing/billing_form.html', {'form': form})

def billing_success(request):
    return render(request, 'billing/billing_success.html')
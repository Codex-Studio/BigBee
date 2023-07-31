from django.shortcuts import render, redirect, get_object_or_404

from apps.settings.models import Setting
from apps.products.models import Product, ProductFavorite

# Create your views here.
def product_detail(request, id):
    setting = Setting.objects.latest('id')
    product = Product.objects.get(id = id)
    related_products = Product.objects.filter(category=product.category)
    return render(request, 'products/detail.html', locals())

def wishlist(request):
    setting = Setting.objects.latest('id')
    if request.user.is_authenticated:
        wishlist_items = ProductFavorite.objects.filter(user=request.user)
    else:
        wishlist_items = []
    return render(request, 'products/wishlist.html', locals())

def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated:
        # For authenticated users, create or get the WishlistItem for the current user and product
        wishlist_item, created = ProductFavorite.objects.get_or_create(user=request.user, product=product)
    else:
        # For anonymous users, store the wishlist items in the session
        wishlist = request.session.get('wishlist', [])
        if product_id not in wishlist:
            wishlist.append(product_id)
            request.session['wishlist'] = wishlist
    
    return redirect('wishlist')
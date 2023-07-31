from django.urls import path 

from apps.products.views import product_detail, wishlist, add_to_wishlist


urlpatterns = [
    path("<int:id>/", product_detail, name="product_detail"),
    path('wishlist/', wishlist, name='wishlist'),
    path('add_to_wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
]
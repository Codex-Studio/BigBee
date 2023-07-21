from django.urls import path
from apps.carts import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
]
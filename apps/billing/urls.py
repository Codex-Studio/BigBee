from django.urls import path 

from apps.billing.views import create_billing, billing_success

urlpatterns = [
    # ... Другие URL-ы ...
    path('create_billing/', create_billing, name='create_billing'),
    path('billing_success/', billing_success, name='billing_success'),
]
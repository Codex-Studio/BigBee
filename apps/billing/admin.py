from django.contrib import admin

from apps.billing.models import Billing

# Register your models here.
@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('user', 'billing_receipt_type','created', 'status')
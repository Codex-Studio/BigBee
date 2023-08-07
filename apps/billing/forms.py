from django import forms

from apps.billing.models import Billing

class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['billing_receipt_type']  # Добавьте другие поля по вашему желанию
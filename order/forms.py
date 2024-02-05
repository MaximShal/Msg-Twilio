from django import forms
from order.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('start_timestamp', 'end_timestamp', 'user_email', 'user_name')
        widgets = {
            'start_timestamp': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_timestamp': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

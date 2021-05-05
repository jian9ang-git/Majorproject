from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['country', 'city', 'street', 'house', 'post_index', 'delivery_time', 'comment']


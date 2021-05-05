from django import forms
from sweet.models import Adress

PRODUCT_QUANTITY_CHOICES = ((i, str(i)) for i in range(1, 21))


class CartAddEditProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)



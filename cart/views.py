from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from sweet.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def basket_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('basket')


def basket_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('basket')


def basket(request):
    cart = Cart(request)
    return render(request, 'basket.html', {'cart': cart})
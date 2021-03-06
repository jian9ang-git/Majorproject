from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from sweet.models import Product, Adress
from .cart import Cart
from .forms import CartAddEditProductForm


def basket(request):
    cart = Cart(request)
    return render(request, 'basket.html', {'cart': cart})


@require_POST
def checkout_edit(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddEditProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=not cd['update'])
    return redirect('checkout_base')


@require_POST
def basket_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddEditProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:basket')


def basket_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:basket')


from django.shortcuts import render, redirect, get_object_or_404
from .models import OrderItem, Order
from sweet.models import Product
from .forms import OrderCreateForm
from cart.cart import Cart
from django.views.decorators.http import require_POST
from cart.forms import CartAddEditProductForm


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
    return redirect('orders:checkout_base')


def checkout_base(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'created_order.html',
                          {'order': order})
    else:
        cart_product_form = CartAddEditProductForm()
        form = OrderCreateForm()
    return render(request, 'checkout_base.html',
                  {'cart': cart, 'form': form, 'cart_product_form': cart_product_form})


def created_order(request):
    return render(request, 'created_order.html')



from django.shortcuts import render,  get_object_or_404, redirect
from .models import Customer, Category, Product
from cart.forms import CartAddEditProductForm


def home(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        all_categories = Category.objects.all()
        return render(request, 'categories.html', {'all_categories': all_categories})


def category_page(request, category_id):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        category = Category.objects.get(id=category_id)
        all_products = Product.objects.filter(product_category=category)
        return render(request, 'category_page.html', {'all_products': all_products})


def product_page(request, product_id):
    if request.method == "GET":
        product = Product.objects.get(id=product_id)
        cart_product_form = CartAddEditProductForm()
        return render(request, 'product_page.html', {'product': product, 'cart_product_form': cart_product_form})

    elif request.method == "POST":
        product = get_object_or_404(Product,
                                    id=product_id,
                                    available=True)
        return render(request, 'product_page.html', {'product': product})

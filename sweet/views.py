from django.shortcuts import render,  get_object_or_404, redirect
from .models import Customer, Category, Product
from cart.forms import CartAddProductForm


def home(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        all_categories = Category.objects.all()
        return render(request, 'base.html', {'all_categories': all_categories})


def category_page(request, category_id):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        category = Category.objects.get(id=category_id)
        all_products = Product.objects.filter(product_category=category)
        return render(request, 'category_page.html', {'all_products': all_products})


def product_page(request, product_id):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        product = Product.objects.get(id=product_id)
        return render(request, 'product_page.html', {'product': product})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'sweet/product/basket.html', {'product': product,
                                                        'cart_product_form': cart_product_form})

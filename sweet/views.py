from django.shortcuts import render
from .models import Customer, Category, Product


def home(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        all_categories = Category.objects.all()
        return render(request, 'base.html', {'all_categories': all_categories})


def basket(request):
    return render(request, 'basket.html')


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


def final(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        return render(request, 'final.html', {})

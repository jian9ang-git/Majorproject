from django.contrib import admin
from .models import Category, Customer, Product, Adress


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'total_orders', 'in_stock_now', 'last_supply', 'next_supply', 'available']
    list_filter = ['available', 'last_supply', 'next_supply']
    list_editable = ['price', 'in_stock_now', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Customer)
admin.site.register(Adress)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

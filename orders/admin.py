from django.contrib import admin
from .models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'delivery_time', 'comment', 'created',
                    'updated', 'paid']
    list_filter = ['delivery_time', 'paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)


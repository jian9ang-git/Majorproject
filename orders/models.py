from django.db import models
from sweet.models import Product, Adress


class Order(models.Model):
    country = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    street = models.CharField(max_length=50, blank=True)
    house = models.CharField(max_length=30, blank=True)
    post_index = models.CharField(max_length=30, blank=True)
    delivery_time = models.CharField(blank=False, max_length=20)
    comment = models.TextField(max_length=250, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL, related_name='items')
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, related_name='order_items')
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

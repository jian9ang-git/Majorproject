from django.db import models
from django.utils import timezone


class Adress(models.Model):
    region = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=50)
    house = models.CharField(max_length=30)
    post_index = models.CharField(max_length=30)

    def __str__(self):
        return self.city


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=200, db_index=True, null=True)
    description = models.TextField(max_length=250, blank=True)
    price = models.IntegerField()
    product_category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        related_name='product',
    )
    total_orders = models.IntegerField()
    in_stock_now = models.IntegerField()
    last_supply = models.DateTimeField()
    next_supply = models.DateTimeField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


#  class AnonimusCustomer(models.Model):
    #  status = models.CharField(max_length=30, default='anon')
    #  ip_adress = models.IPAddressField()


class Customer(models.Model):
    #  status = models.CharField(max_length=30, default='registred')
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'Oth'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )
    username = models.CharField(max_length=30)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    register_date = models.DateTimeField(auto_now_add=True)
    orders_numb = models.IntegerField()
    last_order_date = models.DateTimeField(auto_now=True)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, default=MALE)
    adresses = models.ManyToManyField(
        Adress,
        related_name='customer_adresses'
    )

    def __str__(self):
        return self.username

from django.urls import path
from .views import basket, basket_remove, basket_add

urlpatterns = [
    path('basket', basket, name='basket'),
    path('basket_remove/<product_id>', basket_remove, name='basket_remove'),
    path('basket_add/<product_id>', basket_add, name='basket_add'),
]

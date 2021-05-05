from django.urls import path
from .views import checkout_base, created_order, checkout_edit

urlpatterns = [
    path('checkout_base', checkout_base, name='checkout_base'),
    path('created_order', created_order, name='created_order'),
    path('checkout_edit/<product_id>', checkout_edit, name='checkout_edit'),
]

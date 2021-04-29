from django.urls import path
from .views import home, basket, category_page, product_page


urlpatterns = [
    path('', home, name='home'),
    path('basket', basket, name='basket'),
    path('category_page/<category_id>', category_page, name='category_page'),
    path('product_page/<product_id>', product_page, name='product_page'),
]

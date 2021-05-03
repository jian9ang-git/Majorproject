from django.urls import path
from django.conf.urls import url
from .views import home, category_page, product_page


urlpatterns = [
    path('', home, name='home'),
    path('category_page/<category_id>', category_page, name='category_page'),
    path('product_page/<product_id>', product_page, name='product_page'),
]

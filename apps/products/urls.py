from django.urls import path

from apps.products.views import product_list, create_product


app_name='products'

urlpatterns = [
    path('product_list/', product_list, name='product_list'),
    path('create_product/', create_product, name='create_product'),
]

from django.urls import path

from apps.shopping_cart.views import add_to_cart, order_details


app_name='shopping_cart'

urlpatterns = [
    path('add_to_cart/<int:item_id>/<int:quantity>/', add_to_cart, name='add_to_cart'),
    path('order_summary/', order_details, name='order_summary'),
]

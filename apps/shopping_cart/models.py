from django.db import models

from apps.accounts.models import Profile
from apps.products.models import Product


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def __str__(self):
        return '{0}'.format(self.owner)

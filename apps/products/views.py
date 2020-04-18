
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


from apps.shopping_cart.models import Order, OrderItem
from apps.products.models import Product

@login_required
def product_list(request):
    object_list = Product.objects.all()
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [product.product for product in user_order_items]

    context = {
        'object_list': object_list,
        'current_order_products': current_order_products
    }

    return render(request, "products/product_list.html", context)

from apps.products.forms import ProductForm

@login_required
def create_product(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'products/product_form.html', {'form': form})
    elif request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print(form)
            form.save()
            return redirect("success")



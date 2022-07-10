from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order


class CheckOut(View):

    @classmethod
    def post(cls, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer_id = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(customer_id)
        print(f"address:{address}")
        print(f"address:{phone}")
        print(customer_id)
        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer.objects.get(id=customer_id),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}
        return redirect('cart')

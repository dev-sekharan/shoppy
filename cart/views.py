from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from cart.models import Cart
from product.models import Product

# Create your views here.


class CartView(LoginRequiredMixin, generic.ListView):
    template_name = "cart/index.html"
    model = Cart
    context_object_name = "cart"


def add(request, p_id):
    user = request.user
    product = Product.objects.get(P_ID=p_id)
    cart = Cart(U_ID=user, P_ID=product)
    cart.save()
    return redirect('/')





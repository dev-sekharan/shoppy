from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from cart.models import Cart
from product.models import Product
from django.urls import reverse
from cart import views

# Create your views here.


class CartView(LoginRequiredMixin, generic.ListView):
    template_name = "cart/index.html"
    model = Cart
    context_object_name = "cart"


@login_required
def add(request):
    if request.method == "POST":
        user = request.user
        qty = int(request.POST['qty'])
        product = Product.objects.get(P_ID=request.POST['p_id'])
        try:
            cart = Cart.objects.get(U_ID=user, P_ID=product)
        except ObjectDoesNotExist:
            cart = None
        if product.P_STOCK >= qty:
            if cart is not None:
                cart.C_QTY = qty
                cart.save()
                print("CART UPDATED")
            else:
                Cart.objects.create(U_ID=user, P_ID=product, C_QTY=qty)
                print("NEW PRODUCT ADDED IN THE CART")
            return redirect(reverse('cart:cart'))
        else:
            return HttpResponseRedirect(reverse('product'))





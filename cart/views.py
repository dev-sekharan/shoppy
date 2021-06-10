from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import F
from cart.models import Cart
from product.models import Product
from buy.views import item


# Create your views here.


@login_required
def index(request):
    user = request.user
    try:
        cart = Cart.objects.filter(C_USER=user).annotate(C_PRICE=F('C_PRODUCT__P_PRICE')*F('C_QUANTITY'))
        for x in cart:
            x.counter = range(1, x.C_PRODUCT.P_STOCK)
    except ObjectDoesNotExist:
        cart = None
    return render(request, 'cart/index.html', {'cart': cart})


@login_required
def add(request):
    if request.method == "POST":
        user = request.user
        qty = int(request.POST['qty'])
        product = Product.objects.get(P_ID=request.POST['p_id'])
        try:
            cart = Cart.objects.get(C_USER=user, C_PRODUCT=product)
        except ObjectDoesNotExist:
            cart = None
        if product.P_STOCK >= qty:
            if cart is not None:
                cart.C_QUANTITY = qty
                cart.save()
                messages.info(request, "CART UPDATED")
            else:
                Cart.objects.create(C_USER=user, C_PRODUCT=product, C_QUANTITY=qty)
                messages.info(request, "NEW PRODUCT ADDED IN THE CART")
            return redirect(reverse('cart:cart'))
        else:
            return HttpResponseRedirect(reverse('product'))


@login_required
def process(request):
    if request.method == "POST":
        if request.POST.get("update"):
            return update(request)
        elif request.POST.get("delete"):
            return delete(request)
        else:
            return item(request)
    else:
        return redirect("cart:cart")


@login_required
def update(request):
    cid = request.POST['cid']
    qty = request.POST['qty']
    try:
        cart = Cart.objects.get(id=cid)
    except ObjectDoesNotExist:
        cart = None
    if cart is not None:
        cart.C_QUANTITY = qty
        cart.save()
    else:
        messages.info(request, "NOT SAVED!")
    return redirect('cart:cart')


@login_required
def delete(request):
    cid = request.POST['cid']
    try:
        cart = Cart.objects.get(id=cid).delete()
    except ObjectDoesNotExist:
        messages.info(request, "NO ENTRY!")
    return redirect('cart:cart')

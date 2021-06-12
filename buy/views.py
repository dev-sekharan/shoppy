from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from buy.models import Buy
from cart.models import Cart
from product.models import Product

# Create your views here.

def purchase(user,cart):
    try:
        for c in cart:
            product = c.C_PRODUCT
            price = product.P_PRICE * c.C_QUANTITY
            Buy.objects.create(
                                B_USER = user,
                                B_PRODUCT = c.C_PRODUCT,
                                B_QUANTITY = c.C_QUANTITY,
                                B_PRICE = price
                              )
            c.delete()
    except Exception as e:
        print(e)
        return 0
    return 1


@login_required
def item(request):
    if request.method == 'POST' and request.POST['cid'] is not None:
        user = request.user
        cid = request.POST['cid']
        try:
            cart = Cart.objects.get(id = cid)
        except ObjectDoesNotExist:
            messages.info(request, "Item does not exist")
            return redirect('cart:cart')
        if purchase(user, cart):
            messages.info(request, 'ORDER HAS BEEN PLACED')
        else:
            messages.info(request,'An unexpected error occurred')
        return redirect('cart:cart')
    else:
        return redirect('cart:cart')



@login_required
def cart(request):
    print('cart')
    user = request.user
    try:
        cart = Cart.objects.filter(C_USER = user)
    except ObjectDoesNotExist:
        messages.info(request,"Your cart is empty")
    if purchase(user, cart):
        messages.info(request, "EUREKA")
    else:
        messages.info(request,"An unexpected error occurred")
    return redirect('cart:cart')

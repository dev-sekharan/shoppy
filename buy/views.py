from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from buy.models import Buy
from cart.models import Cart
from product.models import Product

# Create your views here.

@login_required()
def item(request):
    if request.method == 'POST' and request.POST['cid'] is not None:
        user = request.user
        cid = request.POST['cid']
        try:
            cart = Cart.objects.get(id = cid)
        except ObjectDoesNotExist:
            messages.info(request, "Item does not exist")
            return redirect('cart:cart')
        Buy.objects.create(
                            B_USER = user,
                            B_PRODUCT = cart.C_PRODUCT,
                            B_QUANTITY = cart.C_QUANTITY,
                          )
        Cart.objects.get(id = cid).delete()
        messages.info(request, 'ORDER HAS BEEN PLACED')
        print('ORDER HAS BEEN PLACED')
        return redirect('cart:cart')
    else:
        return redirect('cart:cart')

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request,'product/index.html',{'products':products})

def detail(request, P_SLUG):
    product = Product.objects.filter(P_SLUG = P_SLUG)
    return render(request,'product/detail.html',{'product':product})

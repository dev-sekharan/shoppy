from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request,'product/index.html',{'products':products})

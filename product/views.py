from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product


# Create your views here.
class ProductView(generic.ListView):
    template_name = 'product/index.html'
    model = Product
    context_object_name = 'products'


def detail(request, p_slug):
    product = get_object_or_404(Product, P_SLUG = p_slug)
    return render(request, 'product/detail.html', {'product':product})

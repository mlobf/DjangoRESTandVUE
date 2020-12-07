from django.http import JsonResponse
from .models import Product, Manufacturer


def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values())}
    response = JsonResponse(data)
    return response

def product_detail(request,pk):
    pass





"""
from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Product, Manufacturer


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"

"""
#from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Product, Manufacturer


class ProductDetailsView(DetailView):
    models = Product
    template_name = "products/product_details.html"

class ProductListView(ListView):
    models = Product
    template_name = "products/product_list.html"
from django.http import JsonResponse
from .models import Product, Manufacturer


# Product List ---------------------------------------------------------------
def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values())}
    response = JsonResponse(data)
    return response


# Product Details ------------------------------------------------------------
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {
            "product": {
                "name": product.name,
                "manufacturer": product.manufacturer.name,
                "description": product.description,
                "photo": product.photo.url,
                "price": product.price,
                "shipping_cost": product.shipping_cost,
                "quantity": product.quantity,
            }
        }

        response = JsonResponse(data)

    except Product.DoesNotExist:

        response = JsonResponse(
            {"error": {"code": 404, "message": "product not found!"}}, status=404
        )

    return response


# Manufacture  List -----------------------------------------------------------
def manufacturer_list(request):

    manufacturer = Manufacturer.objects.all()
    data = {"products": list(manufacturer.values())}
    response = JsonResponse(data)
    return response


# Manufactured Details ------------------------------------------------------------
def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        manufacturer_products = manufacturer.products.all()
        data = {
            "manufacturer": {
                "name": manufacturer.name,
                "location": manufacturer.location,
                "active": manufacturer.active,
                "products": list(manufacturer_products.values()),
            }
        }

        response = JsonResponse(data)
        print(response)

    except Manufacturer.DoesNotExist:

        response = JsonResponse(
            {"error": {"code": 404, "message": "Manufacturer not found!"}}, status=404
        )

    return response

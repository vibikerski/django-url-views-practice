from django.shortcuts import render
from Products.models import Product, Review
from django.http import HttpResponse

def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    reviews = Review.objects.filter(product=product)
    
    context = {
        "product": product,
        "reviews": reviews,
    }
    
    return render(
        request,
        "Products/product.html",
        context
    )

def get_all_products(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    
    return render(
        request,
        'Products/products.html',
        context
    )
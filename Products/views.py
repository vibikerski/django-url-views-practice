from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.http import Http404
from Products.models import Product, Review

def get_product(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)
    except Http404:
        return redirect('products')

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

def add_review(request):
    if request.method != "POST":
        return redirect('products')
    author = request.POST.get('author-name')
    text = request.POST.get('review')
    rating = int(request.POST.get('rating'))
    product_id = int(request.POST.get('product_id'))
    
    if not (author and text and rating and product_id):
        return HttpResponse('Missing required data', status=400)
    
    try:
        product = get_object_or_404(Product, id=product_id)
        review = Review.objects.create(
            product=product,
            author=author,
            text=text,
            rating=rating
        )
    except Http404:
        return HttpResponse('Server issue', status=500)
    
    return redirect('product', product_id=product_id)

# products/views.py
from django.shortcuts import render,get_object_or_404
from .models import Product

def store_page(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'store/store.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Fetch the product by ID
    return render(request, 'store/product_detail.html', {'product': product})
# products/views.py
from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from .forms import AddProductForm

def store_page(request):
    context = {}
    if request.user.is_authenticated:
        context['username'] = request.user.username
    products = Product.objects.all()  
    return render(request, 'store/store.html', {'products': products})

def product_detail(request, product_id):
    context = {}
    if request.user.is_authenticated:
        context['username'] = request.user.username
    product = get_object_or_404(Product, id=product_id)  # Fetch the product by ID
    return render(request, 'store/product_detail.html', {'product': product})

def product_create(request):
    context = {}
    if request.user.is_authenticated:
        context['username'] = request.user.username
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('store')
    else:
        form = AddProductForm()
    return render(request, 'store/product_create.html', {'form': form})
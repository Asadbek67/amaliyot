from django.shortcuts import render
from .models import Product, Category

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def create_product(request):
    if request.method == 'POST':
        pass
    return render(request, 'create_product.html')

def create_category(request):
    if request.method == 'POST':
        pass
    return render(request, 'create_category.html')

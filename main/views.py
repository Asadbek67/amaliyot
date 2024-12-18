from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def product_detail(request):
    return render(request, 'product_detail.html')

def create_product(request):
    return render(request, 'create_product.html')

def create_category(request):
    return render(request, 'create_category.html')


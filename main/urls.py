from django.contrib import admin
from django.urls import path

from .views import home, product_detail, create_category, create_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('product/<int:product_id>', product_detail, name='product_detail'),
    path('create_category/', create_category, name='create_category'),
    path('create_product/', create_product, name='create_product'),
]

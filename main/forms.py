from django import forms
from .models import Category, Product

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=200)


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    description = forms.CharField(max_length=200, required=False)


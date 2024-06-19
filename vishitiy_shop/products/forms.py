from django import forms

from .models import Product

class ProductFilterForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('color', 'type', 'price', 'size')
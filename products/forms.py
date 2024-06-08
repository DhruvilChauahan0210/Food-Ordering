from django import forms
from .models import Product, ProductMetaInformation, ProductImages

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_slug,', 'product_description', 'product_price', 'product_demo_price']

class ProductMetaInformationForm(forms.ModelForm):
    class Meta:
        model = ProductMetaInformation
        fields = ['product_quantity', 'product_measuring', 'is_restrict', 'restrict_quantity']

class ProductImagesForm(forms.ModelForm):
    class Meta:
        model = ProductImages
        fields = ['product', 'product_image']

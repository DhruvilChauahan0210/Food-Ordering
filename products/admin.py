from django.contrib import admin
from .models import Product, ProductMetaInformation, ProductImages

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'product_demo_price')

@admin.register(ProductMetaInformation)
class ProductMetaInformationAdmin(admin.ModelAdmin):
    list_display = ('product', 'product_quantity', 'product_measuring', 'is_restrict', 'restrict_quantity')

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('product', 'product_image')

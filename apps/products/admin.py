from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''
    list_display = ('name', 'sku', 'brand', 'price', 'created_at')
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'sku', 'brand')
    fields = ('name', 'sku', 'brand', 'price', 'active', 'created_at', 'updated_at')
    ordering = ('created_at',)

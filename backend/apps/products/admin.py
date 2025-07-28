from django.contrib import admin
from .models import Product, ProductField

class ProductFieldInline(admin.TabularInline):
    model = ProductField
    extra = 0
    fields = ['name', 'field_type', 'label', 'is_required', 'sort_order']
    ordering = ['sort_order']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_type', 'is_featured', 'is_active', 'sort_order']
    list_filter = ['product_type', 'is_featured', 'is_active']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductFieldInline]
    ordering = ['sort_order', 'name']

@admin.register(ProductField)
class ProductFieldAdmin(admin.ModelAdmin):
    list_display = ['product', 'label', 'field_type', 'is_required', 'sort_order']
    list_filter = ['field_type', 'is_required', 'product']
    search_fields = ['label', 'name']
    ordering = ['product', 'sort_order']

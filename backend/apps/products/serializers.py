from rest_framework import serializers
from .models import Product, ProductField

class ProductFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductField
        fields = [
            'id', 'name', 'field_type', 'label', 'placeholder',
            'is_required', 'validation_rules', 'options', 'sort_order'
        ]

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'product_type', 'short_description',
            'icon', 'is_featured'
        ]

class ProductDetailSerializer(serializers.ModelSerializer):
    fields = ProductFieldSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'product_type', 'description',
            'short_description', 'icon', 'is_featured', 'fields'
        ]

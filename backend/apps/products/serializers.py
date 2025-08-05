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
    """Сериализатор для списка продуктов (краткая информация)"""
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'product_type', 'short_description',
            'icon', 'is_featured', 'button_text', 'price_range', 
            'processing_time', 'card_background_color', 'icon_background_color'
        ]

class ProductCardSerializer(serializers.ModelSerializer):
    """Сериализатор для карточек продуктов на главной странице"""
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'short_description', 'icon', 
            'button_text', 'card_background_color', 'icon_background_color',
            'price_range', 'processing_time'
        ]

class ProductDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для детальной страницы продукта"""
    fields = ProductFieldSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'product_type', 'description',
            'short_description', 'icon', 'is_featured', 'fields',
            'button_text', 'benefits', 'price_range', 'processing_time',
            'card_background_color', 'icon_background_color',
            'meta_title', 'meta_description'
        ]

class ProductSEOSerializer(serializers.ModelSerializer):
    """Сериализатор для SEO данных продукта"""
    class Meta:
        model = Product
        fields = ['meta_title', 'meta_description', 'name', 'description']

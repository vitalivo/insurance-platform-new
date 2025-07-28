from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer

class ProductListView(generics.ListAPIView):
    """Список всех продуктов"""
    queryset = Product.active.all()
    serializer_class = ProductListSerializer

class ProductDetailView(generics.RetrieveAPIView):
    """Детали продукта с полями формы"""
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'
    
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Product.active.select_related().prefetch_related('fields'), slug=slug)

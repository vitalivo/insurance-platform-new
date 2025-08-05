from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.db.models import Case, When, IntegerField
from .models import Product
from .serializers import (
    ProductListSerializer, 
    ProductDetailSerializer, 
    ProductCardSerializer,
    ProductSEOSerializer
)
from apps.core.models import SiteSettings

class ProductListView(generics.ListAPIView):
    """Список всех продуктов с учетом настроек сортировки"""
    serializer_class = ProductListSerializer
    
    def get_queryset(self):
        # Получаем настройки сайта
        try:
            settings = SiteSettings.objects.first()
        except SiteSettings.DoesNotExist:
            settings = None
        
        queryset = Product.active.all()
        
        # Применяем сортировку из настроек
        if settings:
            if settings.show_featured_first:
                # Сначала рекомендуемые, потом остальные
                queryset = queryset.annotate(
                    featured_order=Case(
                        When(is_featured=True, then=0),
                        default=1,
                        output_field=IntegerField()
                    )
                ).order_by('featured_order', settings.products_sort_by)
            else:
                queryset = queryset.order_by(settings.products_sort_by)
        else:
            # Сортировка по умолчанию
            queryset = queryset.order_by('sort_order', 'name')
        
        return queryset

class ProductDetailView(generics.RetrieveAPIView):
    """Детали продукта с полями формы"""
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'
    
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(
            Product.active.select_related().prefetch_related('fields__product'), 
            slug=slug
        )

class ProductCardView(generics.ListAPIView):
    """Продукты для отображения в карточках на главной странице"""
    serializer_class = ProductCardSerializer
    
    def get_queryset(self):
        # Получаем настройки сайта
        try:
            settings = SiteSettings.objects.first()
        except SiteSettings.DoesNotExist:
            settings = None
        
        queryset = Product.active.all()
        
        # Применяем сортировку
        if settings and settings.show_featured_first:
            queryset = queryset.annotate(
                featured_order=Case(
                    When(is_featured=True, then=0),
                    default=1,
                    output_field=IntegerField()
                )
            ).order_by('featured_order', 'sort_order', 'name')
        else:
            queryset = queryset.order_by('sort_order', 'name')
        
        return queryset

@api_view(['GET'])
def product_seo_view(request, slug):
    """Получение SEO данных продукта"""
    product = get_object_or_404(Product.active, slug=slug)
    serializer = ProductSEOSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def featured_products_view(request):
    """Получение только рекомендуемых продуктов"""
    products = Product.active.filter(is_featured=True).order_by('sort_order')
    serializer = ProductCardSerializer(products, many=True)
    return Response(serializer.data)

# Функция экспорта заявок (уже существующая)
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
import csv
from apps.applications.models import Application

@staff_member_required
def export_applications(request):
    """Экспорт заявок в CSV"""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="applications.csv"'
    response.write('\ufeff')  # BOM для корректного отображения в Excel
    
    writer = csv.writer(response)
    writer.writerow([
        'Номер заявки', 'Дата', 'Продукт', 'ФИО', 
        'Телефон', 'Email', 'Статус', 'Комментарий'
    ])
    
    applications = Application.objects.select_related('product', 'status').order_by('-created_at')
    
    for app in applications:
        writer.writerow([
            app.application_number,
            app.created_at.strftime('%d.%m.%Y %H:%M'),
            app.product.name,
            app.full_name,
            app.phone,
            app.email,
            app.status.name,
            app.admin_comment or ''
        ])
    
    return response

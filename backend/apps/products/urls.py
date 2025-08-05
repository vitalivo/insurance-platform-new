from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCardView,
    product_seo_view,
    featured_products_view,
    export_applications
)

app_name = 'products'

urlpatterns = [
    # Основные endpoints
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<str:slug>/', ProductDetailView.as_view(), name='product-detail'),
    
    # Дополнительные endpoints
    path('products-cards/', ProductCardView.as_view(), name='product-cards'),
    path('products/<str:slug>/seo/', product_seo_view, name='product-seo'),
    path('featured-products/', featured_products_view, name='featured-products'),
    
    # Экспорт (для админки)
    path('export/applications/', export_applications, name='export-applications'),
]

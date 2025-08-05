from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Product, ProductField
from .views import export_applications

class ProductFieldInline(admin.TabularInline):
    model = ProductField
    extra = 0
    fields = ['name', 'field_type', 'label', 'is_required', 'sort_order']
    ordering = ['sort_order']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'product_type', 'is_featured', 'is_active', 
        'sort_order', 'button_text', 'price_range'
    ]
    list_filter = ['product_type', 'is_featured', 'is_active']
    search_fields = ['name', 'description', 'short_description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductFieldInline]
    ordering = ['sort_order', 'name']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'slug', 'product_type', 'is_active', 'is_featured', 'sort_order')
        }),
        ('Описания', {
            'fields': ('short_description', 'description')
        }),
        ('Отображение', {
            'fields': ('icon', 'button_text'),
            'description': 'Настройки внешнего вида карточки продукта'
        }),
        ('Цвета', {
            'fields': ('card_background_color', 'icon_background_color'),
            'classes': ('collapse',),
            'description': 'Цвета в формате HEX (например: #ffffff)'
        }),
        ('Дополнительная информация', {
            'fields': ('benefits', 'price_range', 'processing_time'),
            'description': 'Дополнительные данные для отображения'
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',),
            'description': 'Настройки для поисковых систем'
        }),
    )
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Добавляем help_text для полей
        form.base_fields['benefits'].help_text = 'JSON массив преимуществ: ["Быстро", "Надежно", "Выгодно"]'
        form.base_fields['card_background_color'].help_text = 'Цвет фона карточки в формате HEX'
        form.base_fields['icon_background_color'].help_text = 'Цвет фона иконки в формате HEX'
        form.base_fields['processing_time'].help_text = 'Например: "5 минут", "1 день"'
        form.base_fields['price_range'].help_text = 'Например: "от 1000 руб.", "по тарифам ЦБ РФ"'
        return form

@admin.register(ProductField)
class ProductFieldAdmin(admin.ModelAdmin):
    list_display = ['product', 'label', 'field_type', 'is_required', 'sort_order']
    list_filter = ['field_type', 'is_required', 'product']
    search_fields = ['label', 'name']
    ordering = ['product', 'sort_order']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('product', 'name', 'field_type', 'label', 'is_required')
        }),
        ('Настройки отображения', {
            'fields': ('placeholder', 'sort_order')
        }),
        ('Дополнительные настройки', {
            'fields': ('validation_rules', 'options'),
            'classes': ('collapse',)
        }),
    )
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['validation_rules'].help_text = 'JSON объект с правилами валидации'
        form.base_fields['options'].help_text = 'JSON массив опций для select: ["Опция 1", "Опция 2"]'
        return form

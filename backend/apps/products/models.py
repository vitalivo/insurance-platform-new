from django.db import models
from apps.core.models import BaseModel

class Product(BaseModel):
    """Страховой продукт"""
    PRODUCT_TYPES = [
        ('osago', 'ОСАГО'),
        ('kasko', 'КАСКО'),
        ('property', 'Недвижимость'),
        ('accident', 'Несчастный случай'),
        ('mortgage', 'Ипотека'),
        ('tick', 'Клещ'),
    ]
    
    name = models.CharField('Название', max_length=100)
    slug = models.SlugField('URL slug', unique=True)
    product_type = models.CharField('Тип продукта', max_length=20, choices=PRODUCT_TYPES)
    description = models.TextField('Описание')
    short_description = models.CharField('Краткое описание', max_length=200)
    icon = models.CharField('Иконка', max_length=50, help_text='Название иконки для фронтенда')
    is_featured = models.BooleanField('Рекомендуемый', default=False)
    sort_order = models.PositiveIntegerField('Порядок сортировки', default=0)
    
    class Meta:
        verbose_name = 'Страховой продукт'
        verbose_name_plural = 'Страховые продукты'
        ordering = ['sort_order', 'name']
    
    def __str__(self):
        return self.name

class ProductField(BaseModel):
    """Поля формы для продукта"""
    FIELD_TYPES = [
        ('text', 'Текстовое поле'),
        ('email', 'Email'),
        ('phone', 'Телефон'),
        ('number', 'Число'),
        ('date', 'Дата'),
        ('select', 'Выпадающий список'),
        ('checkbox', 'Чекбокс'),
        ('textarea', 'Многострочный текст'),
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='fields')
    name = models.CharField('Название поля', max_length=100)
    field_type = models.CharField('Тип поля', max_length=20, choices=FIELD_TYPES)
    label = models.CharField('Подпись', max_length=100)
    placeholder = models.CharField('Placeholder', max_length=100, blank=True)
    is_required = models.BooleanField('Обязательное', default=True)
    validation_rules = models.JSONField('Правила валидации', default=dict, blank=True)
    options = models.JSONField('Опции для select', default=list, blank=True)
    sort_order = models.PositiveIntegerField('Порядок', default=0)
    
    class Meta:
        verbose_name = 'Поле продукта'
        verbose_name_plural = 'Поля продуктов'
        ordering = ['product', 'sort_order']
    
    def __str__(self):
        return f"{self.product.name} - {self.label}"

from django.db import models
from django.utils import timezone

class TimeStampedModel(models.Model):
    """Абстрактная модель с временными метками"""
    created_at = models.DateTimeField('Дата создания', default=timezone.now)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        abstract = True

class ActiveManager(models.Manager):
    """Менеджер для активных записей"""
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class BaseModel(TimeStampedModel):
    """Базовая модель с общими полями"""
    is_active = models.BooleanField('Активно', default=True)
    
    objects = models.Manager()
    active = ActiveManager()

    class Meta:
        abstract = True

# backend/apps/core/models.py
class PageContent(models.Model):
    page_name = models.CharField('Страница', max_length=100)
    section_name = models.CharField('Секция', max_length=100)
    content_key = models.CharField('Ключ контента', max_length=100)
    content_value = models.TextField('Значение')
    content_type = models.CharField('Тип', max_length=20, choices=[
        ('text', 'Текст'),
        ('html', 'HTML'),
        ('number', 'Число'),
        ('boolean', 'Да/Нет')
    ])
    
    class Meta:
        unique_together = ['page_name', 'section_name', 'content_key']
        
# backend/apps/core/models.py
class SiteSettings(models.Model):
    # Настройки отображения продуктов
    products_per_row_desktop = models.IntegerField('Колонок на десктопе', default=3)
    products_per_row_tablet = models.IntegerField('Колонок на планшете', default=2)
    products_per_row_mobile = models.IntegerField('Колонок на мобильном', default=1)
    
    # Сортировка
    products_sort_by = models.CharField('Сортировать по', max_length=20, choices=[
        ('sort_order', 'Порядок'),
        ('name', 'Название'),
        ('created_at', 'Дата создания')
    ], default='sort_order')
    
    show_featured_first = models.BooleanField('Показывать рекомендуемые первыми', default=True)        
        
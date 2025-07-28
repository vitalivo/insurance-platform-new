from django.db import models
from apps.core.models import BaseModel
from apps.products.models import Product

class ApplicationStatus(BaseModel):
    """Статусы заявок"""
    name = models.CharField('Название', max_length=50, unique=True)
    color = models.CharField('Цвет', max_length=7, default='#6B7280')
    description = models.TextField('Описание', blank=True)
    is_final = models.BooleanField('Финальный статус', default=False)
    sort_order = models.PositiveIntegerField('Порядок', default=0, db_column='order')  # Указываем db_column
    
    class Meta:
        verbose_name = 'Статус заявки'
        verbose_name_plural = 'Статусы заявок'
        ordering = ['sort_order']
    
    def __str__(self):
        return self.name

class Application(BaseModel):
    """Заявка на страхование"""
    application_number = models.CharField('Номер заявки', max_length=50, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    status = models.ForeignKey(ApplicationStatus, on_delete=models.PROTECT, verbose_name='Статус')
    
    # Основные поля клиента
    full_name = models.CharField('ФИО', max_length=200)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email')
    
    # Дополнительные данные (JSON)
    form_data = models.JSONField('Данные формы', default=dict)
    
    # Служебные поля
    admin_comment = models.TextField('Комментарий администратора', blank=True)
    processed_at = models.DateTimeField('Дата обработки', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.application_number} - {self.full_name}"
    
    def save(self, *args, **kwargs):
        if not self.application_number:
            from apps.core.utils import generate_application_number
            self.application_number = generate_application_number()
        super().save(*args, **kwargs)



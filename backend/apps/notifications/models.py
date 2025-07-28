from django.db import models
from apps.core.models import BaseModel

class NotificationTemplate(BaseModel):
    """Шаблоны уведомлений"""
    TEMPLATE_TYPES = [
        ('email_client', 'Email клиенту'),
        ('email_admin', 'Email администратору'),
        ('telegram_admin', 'Telegram администратору'),
    ]
    
    name = models.CharField('Название', max_length=100)
    template_type = models.CharField('Тип шаблона', max_length=20, choices=TEMPLATE_TYPES)
    subject = models.CharField('Тема', max_length=200, blank=True)
    content = models.TextField('Содержание')
    is_html = models.BooleanField('HTML формат', default=True)
    
    class Meta:
        verbose_name = 'Шаблон уведомления'
        verbose_name_plural = 'Шаблоны уведомлений'
    
    def __str__(self):
        return self.name

class NotificationLog(BaseModel):
    """Лог отправленных уведомлений"""
    NOTIFICATION_TYPES = [
        ('email', 'Email'),
        ('telegram', 'Telegram'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('sent', 'Отправлено'),
        ('failed', 'Ошибка'),
    ]
    
    notification_type = models.CharField('Тип', max_length=20, choices=NOTIFICATION_TYPES)
    recipient = models.CharField('Получатель', max_length=200)
    subject = models.CharField('Тема', max_length=200, blank=True)
    content = models.TextField('Содержание')
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='pending')
    error_message = models.TextField('Сообщение об ошибке', blank=True)
    sent_at = models.DateTimeField('Дата отправки', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Лог уведомления'
        verbose_name_plural = 'Логи уведомлений'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.get_notification_type_display()} - {self.recipient}"

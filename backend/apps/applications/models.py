from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.core.models import BaseModel
from apps.products.models import Product

class ApplicationStatus(BaseModel):
    """Статусы заявок"""
    name = models.CharField('Название', max_length=50, unique=True)
    color = models.CharField('Цвет', max_length=7, default='#6B7280')
    description = models.TextField('Описание', blank=True)
    is_final = models.BooleanField('Финальный статус', default=False)
    sort_order = models.PositiveIntegerField('Порядок', default=0, db_column='order')

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
    
    # Поля для отслеживания отправки уведомлений
    notifications_sent = models.BooleanField('Уведомления отправлены', default=False)
    client_notified = models.BooleanField('Клиент уведомлен', default=False)
    admin_notified = models.BooleanField('Админ уведомлен', default=False)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.application_number} - {self.full_name}"

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        old_status = None
        
        if not is_new:
            # Получаем старый статус для отслеживания изменений
            try:
                old_instance = Application.objects.get(pk=self.pk)
                old_status = old_instance.status.name if old_instance.status != self.status else None
            except Application.DoesNotExist:
                pass
        
        if not self.application_number:
            from apps.core.utils import generate_application_number
            self.application_number = generate_application_number()
        
        super().save(*args, **kwargs)
        
        # Отправляем уведомление об изменении статуса (только если статус изменился)
        if old_status and old_status != self.status.name:
            self._send_status_change_notification(old_status)

    def _send_status_change_notification(self, old_status):
        """Отправка уведомления об изменении статуса"""
        try:
            from apps.notifications.services import EmailService
            
            context = {
                'application_number': self.application_number,
                'product_name': self.product.name,
                'client_name': self.full_name,
                'old_status': old_status,
                'new_status': self.status.name,
                'admin_comment': self.admin_comment,
                'site_name': 'СтрахПлатформа',
                'site_url': 'http://localhost:3000',
            }
            
            EmailService.send_email(
                recipient_email=self.email,
                template_name='status_change_client',
                context=context
            )
            
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Ошибка отправки уведомления об изменении статуса: {e}")

# Сигнал для отправки уведомлений при создании новой заявки
@receiver(post_save, sender=Application)
def application_post_save(sender, instance, created, **kwargs):
    """Сигнал после сохранения заявки"""
    if created and not instance.notifications_sent:
        # Отправляем уведомления синхронно
        instance._send_notifications_sync()

# Добавляем метод для синхронной отправки уведомлений
def _send_notifications_sync(self):
    """Синхронная отправка уведомлений"""
    try:
        from apps.notifications.services import NotificationService
        
        # Отправляем все уведомления
        results = NotificationService.send_all_notifications(self)
        
        # Обновляем статус отправки
        if results['client_email']:
            self.client_notified = True
        if results['admin_email'] or results['telegram']:
            self.admin_notified = True
        if any(results.values()):
            self.notifications_sent = True
            
        # Сохраняем изменения
        Application.objects.filter(pk=self.pk).update(
            notifications_sent=self.notifications_sent,
            client_notified=self.client_notified,
            admin_notified=self.admin_notified
        )
        
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Ошибка синхронной отправки уведомлений: {e}")

# Добавляем метод к классу Application
Application._send_notifications_sync = _send_notifications_sync

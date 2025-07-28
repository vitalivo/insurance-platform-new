from celery import shared_task
from django.conf import settings
from apps.applications.models import Application
from .services import EmailService, TelegramService

@shared_task
def send_application_notifications(application_id: int):
    """Отправка уведомлений о новой заявке"""
    try:
        application = Application.objects.select_related('product', 'status').get(id=application_id)
        
        # Контекст для шаблонов
        context = {
            'application_number': application.application_number,
            'product_name': application.product.name,
            'client_name': application.full_name,
            'client_phone': application.phone,
            'client_email': application.email,
            'created_at': application.created_at.strftime('%d.%m.%Y %H:%M'),
        }
        
        # Отправляем email клиенту
        EmailService.send_email(
            recipient_email=application.email,
            template_name='new_application_client',
            context=context
        )
        
        # Отправляем уведомление в Telegram администратору
        telegram_message = f"""
🆕 <b>Новая заявка!</b>

📋 Номер: {application.application_number}
🛡️ Продукт: {application.product.name}
👤 Клиент: {application.full_name}
📞 Телефон: {application.phone}
📧 Email: {application.email}
📅 Дата: {application.created_at.strftime('%d.%m.%Y %H:%M')}
        """
        
        TelegramService.send_telegram_message(telegram_message)
        
    except Application.DoesNotExist:
        pass
    except Exception as e:
        # Логируем ошибку, но не падаем
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Error sending notifications for application {application_id}: {e}")

@shared_task
def send_status_change_notification(application_id: int, old_status: str, new_status: str):
    """Уведомление об изменении статуса заявки"""
    try:
        application = Application.objects.select_related('product', 'status').get(id=application_id)
        
        context = {
            'application_number': application.application_number,
            'product_name': application.product.name,
            'client_name': application.full_name,
            'old_status': old_status,
            'new_status': new_status,
            'admin_comment': application.admin_comment,
        }
        
        # Отправляем email клиенту
        EmailService.send_email(
            recipient_email=application.email,
            template_name='status_change_client',
            context=context
        )
        
    except Application.DoesNotExist:
        pass
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Error sending status change notification for application {application_id}: {e}")

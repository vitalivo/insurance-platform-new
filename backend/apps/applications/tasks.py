from celery import shared_task
from django.conf import settings
from apps.applications.models import Application
from apps.notifications.services import EmailService, TelegramService
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True, max_retries=3)
def send_application_notifications(self, application_id: int):
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
            'site_name': getattr(settings, 'SITE_NAME', 'СтрахПлатформа'),
            'site_url': getattr(settings, 'SITE_URL', 'http://localhost:3000'),
            'admin_url': f"{getattr(settings, 'SITE_URL', 'http://localhost:3000').replace(':3000', ':8000')}/admin/applications/application/{application.id}/change/",
        }
        
        results = {
            'client_email': False,
            'admin_email': False,
            'telegram': False
        }
        
        # Отправляем email клиенту
        try:
            results['client_email'] = EmailService.send_email(
                recipient_email=application.email,
                template_name='new_application_client',
                context=context
            )
            if results['client_email']:
                application.client_notified = True
        except Exception as e:
            logger.error(f"Ошибка отправки email клиенту: {e}")
        
        # Отправляем email администратору
        try:
            admin_email = getattr(settings, 'ADMIN_EMAIL', None)
            if admin_email:
                results['admin_email'] = EmailService.send_email(
                    recipient_email=admin_email,
                    template_name='new_application_admin',
                    context=context
                )
        except Exception as e:
            logger.error(f"Ошибка отправки email админу: {e}")
        
        # Отправляем уведомление в Telegram администратору
        try:
            telegram_message = f"""🆕 <b>Новая заявка!</b>

📋 Номер: {application.application_number}
🛡️ Продукт: {application.product.name}
👤 Клиент: {application.full_name}
📞 Телефон: {application.phone}
📧 Email: {application.email}
📅 Дата: {application.created_at.strftime('%d.%m.%Y %H:%M')}

<a href="{context['admin_url']}">Открыть в админке</a>"""
            
            results['telegram'] = TelegramService.send_telegram_message(telegram_message)
            if results['telegram']:
                application.admin_notified = True
        except Exception as e:
            logger.error(f"Ошибка отправки Telegram: {e}")
        
        # Обновляем статус отправки уведомлений
        if any(results.values()):
            application.notifications_sent = True
            application.save(update_fields=['notifications_sent', 'client_notified', 'admin_notified'])
        
        logger.info(f"Уведомления для заявки {application.application_number}: {results}")
        return results
        
    except Application.DoesNotExist:
        logger.error(f"Заявка с ID {application_id} не найдена")
        return False
        
    except Exception as exc:
        logger.error(f"Ошибка отправки уведомлений: {str(exc)}")
        # Повторяем задачу с экспоненциальной задержкой
        raise self.retry(exc=exc, countdown=60 * (2 ** self.request.retries))

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
            'site_name': getattr(settings, 'SITE_NAME', 'СтрахПлатформа'),
            'site_url': getattr(settings, 'SITE_URL', 'http://localhost:3000'),
        }
        
        # Отправляем email клиенту об изменении статуса
        result = EmailService.send_email(
            recipient_email=application.email,
            template_name='status_change_client',
            context=context
        )
        
        logger.info(f"Уведомление об изменении статуса отправлено для заявки {application.application_number}")
        return result
        
    except Application.DoesNotExist:
        logger.error(f"Заявка с ID {application_id} не найдена")
        return False
    except Exception as e:
        logger.error(f"Ошибка отправки уведомления об изменении статуса для заявки {application_id}: {e}")
        return False

import logging
from django.core.mail import send_mail
from django.conf import settings
from django.template import Template, Context
from telegram import Bot
from .models import NotificationTemplate, NotificationLog

logger = logging.getLogger(__name__)

class EmailService:
    """Сервис для отправки email"""
    
    @staticmethod
    def send_email(recipient_email: str, template_name: str, context: dict):
        try:
            template = NotificationTemplate.objects.get(
                template_type='email_client',
                name=template_name,
                is_active=True
            )
            
            # Рендерим шаблон
            subject_template = Template(template.subject)
            content_template = Template(template.content)
            
            subject = subject_template.render(Context(context))
            content = content_template.render(Context(context))
            
            # Отправляем email
            send_mail(
                subject=subject,
                message=content if not template.is_html else '',
                html_message=content if template.is_html else None,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient_email],
                fail_silently=False,
            )
            
            # Логируем успешную отправку
            NotificationLog.objects.create(
                notification_type='email',
                recipient=recipient_email,
                subject=subject,
                content=content,
                status='sent'
            )
            
            logger.info(f"Email sent to {recipient_email}")
            return True
            
        except Exception as e:
            # Логируем ошибку
            NotificationLog.objects.create(
                notification_type='email',
                recipient=recipient_email,
                subject=template.subject if 'template' in locals() else '',
                content=str(e),
                status='failed',
                error_message=str(e)
            )
            
            logger.error(f"Failed to send email to {recipient_email}: {e}")
            return False

class TelegramService:
    """Сервис для отправки Telegram уведомлений"""
    
    @staticmethod
    def send_telegram_message(message: str, chat_id: str = None):
        try:
            if not settings.TELEGRAM_BOT_TOKEN:
                logger.warning("Telegram bot token not configured")
                return False
            
            bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
            target_chat_id = chat_id or settings.TELEGRAM_CHAT_ID
            
            if not target_chat_id:
                logger.warning("Telegram chat ID not configured")
                return False
            
            bot.send_message(
                chat_id=target_chat_id,
                text=message,
                parse_mode='HTML'
            )
            
            # Логируем успешную отправку
            NotificationLog.objects.create(
                notification_type='telegram',
                recipient=target_chat_id,
                content=message,
                status='sent'
            )
            
            logger.info(f"Telegram message sent to {target_chat_id}")
            return True
            
        except Exception as e:
            # Логируем ошибку
            NotificationLog.objects.create(
                notification_type='telegram',
                recipient=target_chat_id if 'target_chat_id' in locals() else 'unknown',
                content=message,
                status='failed',
                error_message=str(e)
            )
            
            logger.error(f"Failed to send Telegram message: {e}")
            return False

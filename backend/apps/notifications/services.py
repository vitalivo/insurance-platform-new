import logging
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger(__name__)

class EmailService:
    """Сервис для отправки email уведомлений"""
    
    @staticmethod
    def send_email(recipient_email, template_name, context):
        """Отправка email с использованием шаблона"""
        try:
            # Определяем тему и содержание в зависимости от типа шаблона
            if template_name == 'new_application_client':
                subject = f"Заявка #{context['application_number']} получена"
                message = f"""
Здравствуйте, {context['client_name']}!

Ваша заявка на {context['product_name']} успешно получена.

Номер заявки: {context['application_number']}
Дата подачи: {context['created_at']}

Наш специалист свяжется с вами в ближайшее время для уточнения деталей.

С уважением,
Команда {context.get('site_name', 'СтрахПлатформа')}
                """.strip()
                
            elif template_name == 'new_application_admin':
                subject = f"Новая заявка #{context['application_number']}"
                message = f"""
Получена новая заявка!

Номер заявки: {context['application_number']}
Продукт: {context['product_name']}
Клиент: {context['client_name']}
Телефон: {context['client_phone']}
Email: {context['client_email']}
Дата: {context['created_at']}

Ссылка на заявку: {context.get('admin_url', '')}
                """.strip()
                
            elif template_name == 'status_change_client':
                subject = f"Статус заявки #{context['application_number']} изменен"
                message = f"""
Здравствуйте, {context['client_name']}!

Статус вашей заявки #{context['application_number']} изменен.

Новый статус: {context['new_status']}

{context.get('admin_comment', '')}

С уважением,
Команда {context.get('site_name', 'СтрахПлатформа')}
                """.strip()
            else:
                subject = "Уведомление"
                message = "Уведомление от страховой платформы"
            
            # Простая отправка через стандартный Django
            logger.info(f"Отправка email на {recipient_email} с темой: {subject}")
            
            success = send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient_email],
                fail_silently=False,
            )
            
            if success:
                logger.info(f"✅ Email успешно отправлен на {recipient_email}")
            else:
                logger.error(f"❌ Не удалось отправить email на {recipient_email}")
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка отправки email на {recipient_email}: {str(e)}")
            return False

class TelegramService:
    """Сервис для отправки уведомлений в Telegram"""
    
    @staticmethod
    def send_telegram_message(message):
        """Отправка сообщения в Telegram"""
        try:
            # Проверяем, установлен ли requests
            try:
                import requests
            except ImportError:
                logger.warning("Библиотека requests не установлена. Telegram уведомления отключены.")
                return False
            
            if not settings.TELEGRAM_BOT_TOKEN or not settings.TELEGRAM_CHAT_ID:
                logger.info("Telegram настройки не заданы. Пропускаем Telegram уведомление.")
                return False
            
            url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
            data = {
                'chat_id': settings.TELEGRAM_CHAT_ID,
                'text': message,
                'parse_mode': 'HTML',
                'disable_web_page_preview': True
            }
            
            response = requests.post(url, data=data, timeout=10)
            success = response.status_code == 200
            
            if success:
                logger.info("✅ Telegram уведомление отправлено")
            else:
                logger.error(f"❌ Ошибка отправки Telegram: {response.text}")
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка отправки Telegram уведомления: {str(e)}")
            return False

class NotificationService:
    """Основной сервис уведомлений"""
    
    @staticmethod
    def send_all_notifications(application):
        """Отправка всех уведомлений для новой заявки"""
        logger.info(f"🚀 Отправка уведомлений для заявки: {application.application_number}")
        
        results = {
            'client_email': False,
            'admin_email': False,
            'telegram': False
        }
        
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
        
        # Отправляем email клиенту
        logger.info("📧 Отправка email клиенту...")
        try:
            results['client_email'] = EmailService.send_email(
                recipient_email=application.email,
                template_name='new_application_client',
                context=context
            )
        except Exception as e:
            logger.error(f"❌ Ошибка отправки email клиенту: {e}")
        
        # Отправляем email администратору
        logger.info("📧 Отправка email администратору...")
        try:
            admin_email = getattr(settings, 'ADMIN_EMAIL', 'admin@strahplatforma.ru')
            results['admin_email'] = EmailService.send_email(
                recipient_email=admin_email,
                template_name='new_application_admin',
                context=context
            )
        except Exception as e:
            logger.error(f"❌ Ошибка отправки email админу: {e}")
        
        # Отправляем уведомление в Telegram
        logger.info("📱 Отправка Telegram уведомления...")
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
        except Exception as e:
            logger.error(f"❌ Ошибка отправки Telegram: {e}")
        
        logger.info(f"✅ Результаты уведомлений: {results}")
        return results
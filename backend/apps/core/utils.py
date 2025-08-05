import re
import uuid
from datetime import datetime

def validate_phone(phone):
    """Валидация номера телефона - поддержка международных номеров"""
    if not phone:
        return False
    
    # Убираем все символы кроме цифр и +
    clean_phone = re.sub(r'[^\d+]', '', phone)
    
    # Проверяем международные номера
    patterns = [
        # Российские номера
        r'^\+7\d{10}$',  # +7XXXXXXXXXX
        r'^8\d{10}$',    # 8XXXXXXXXXX
        r'^7\d{10}$',    # 7XXXXXXXXXX
        r'^\d{10}$',     # XXXXXXXXXX (российские без кода)
        
        # Международные номера
        r'^\+\d{7,15}$',  # Международный формат +XXXXXXX до +XXXXXXXXXXXXXXX
        r'^\d{7,15}$',    # Без плюса, но международный формат
    ]
    
    for pattern in patterns:
        if re.match(pattern, clean_phone):
            return True
    
    return False

def format_phone(phone):
    """Форматирование номера телефона"""
    if not phone:
        return phone
    
    # Убираем все символы кроме цифр и +
    clean_phone = re.sub(r'[^\d+]', '', phone)
    
    # Если номер уже начинается с +, оставляем как есть
    if clean_phone.startswith('+'):
        return clean_phone
    
    # Приводим российские номера к единому формату +7XXXXXXXXXX
    if clean_phone.startswith('8') and len(clean_phone) == 11:
        clean_phone = '+7' + clean_phone[1:]
    elif clean_phone.startswith('7') and len(clean_phone) == 11:
        clean_phone = '+' + clean_phone
    elif len(clean_phone) == 10:
        # Предполагаем, что это российский номер без кода
        clean_phone = '+7' + clean_phone
    else:
        # Для других международных номеров добавляем + если его нет
        if not clean_phone.startswith('+'):
            clean_phone = '+' + clean_phone
    
    return clean_phone

def validate_email(email):
    """Валидация email адреса"""
    if not email:
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def generate_application_number():
    """Генерация номера заявки"""
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    random_part = str(uuid.uuid4().hex)[:4].upper()
    return f"APP-{timestamp}-{random_part}"

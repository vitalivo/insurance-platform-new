import re
from typing import Optional

def validate_phone(phone: str) -> bool:
    """Валидация российского номера телефона"""
    pattern = r'^(\+7|7|8)?[\s\-]?$$?[489][0-9]{2}$$?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$'
    return bool(re.match(pattern, phone))

def format_phone(phone: str) -> str:
    """Форматирование номера телефона"""
    digits = re.sub(r'\D', '', phone)
    if digits.startswith('8'):
        digits = '7' + digits[1:]
    elif digits.startswith('9'):
        digits = '7' + digits
    return f"+{digits}"

def validate_email(email: str) -> bool:
    """Валидация email"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def generate_application_number() -> str:
    """Генерация номера заявки"""
    from datetime import datetime
    return f"APP-{datetime.now().strftime('%Y%m%d%H%M%S')}"

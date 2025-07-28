# 🏢 Страховая платформа - Техническая документация для разработчика

## 🏗️ Архитектура проекта

### Backend (Django REST API)
\`\`\`
backend/
├── apps/
│   ├── core/           # Базовые модели, утилиты, миксины
│   ├── products/       # Страховые продукты и их поля
│   ├── applications/   # Заявки клиентов и статусы
│   ├── accounts/       # Профили администраторов
│   └── notifications/  # Email/Telegram уведомления
├── config/             # Настройки Django, Celery, URLs
├── templates/          # HTML шаблоны для email
├── static/            # Статические файлы
├── media/             # Загруженные файлы
└── logs/              # Логи приложения
\`\`\`

## 🛠️ Технический стек

### Backend
- **Django 4.2.7** - основной фреймворк
- **Django REST Framework 3.14.0** - API
- **PostgreSQL** - основная база данных
- **Redis** - кеширование и очереди
- **Celery** - фоновые задачи
- **python-telegram-bot** - Telegram уведомления

### Зависимости
```python
Django==5.2.4
djangorestframework==3.16.0
django-cors-headers==4.7.0
psycopg2-binary==2.9.10
python-decouple==3.8
celery==5.5.3
redis==6.2.0
python-telegram-bot==22.3
openpyxl==3.1.5
Pillow==11.3.0
django-extensions==4.1

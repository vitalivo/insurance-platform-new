# 🏢 Страховая платформа - Backend

Django REST API для управления страховыми продуктами и заявками.

## 🚀 Быстрый запуск

### 1. Клонирование и настройка

\`\`\`bash
# Создайте виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows

# Установите зависимости
pip install -r requirements.txt

# Скопируйте файл переменных окружения
cp .env.example .env
# Отредактируйте .env файл под ваши настройки
\`\`\`

### 2. Настройка базы данных

\`\`\`bash
# Создайте базу данных PostgreSQL
createdb insurance_platform

# Примените миграции
python manage.py makemigrations
python manage.py migrate

# Загрузите начальные данные
python manage.py load_initial_data

# Создайте суперпользователя
python manage.py createsuperuser
\`\`\`

### 3. Запуск сервера

\`\`\`bash
# Обычный запуск
python manage.py runserver

# Или используйте скрипт автоматической настройки
chmod +x start.sh
./start.sh
\`\`\`

## 📋 API Endpoints

### Продукты
- `GET /api/products/` - Список всех продуктов
- `GET /api/products/{slug}/` - Детали продукта с полями формы

### Заявки
- `POST /api/applications/` - Создание новой заявки
- `GET /api/applications/{number}/` - Поиск заявки по номеру
- `GET /api/export/applications/` - Экспорт заявок в Excel

### Статусы
- `GET /api/statuses/` - Список статусов заявок

### Профиль администратора
- `GET /api/profile/` - Получение профиля
- `PUT /api/profile/` - Обновление профиля

## 🔧 Настройка уведомлений

### Email (Yandex)
\`\`\`env
EMAIL_HOST=smtp.yandex.ru
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@yandex.ru
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_USE_TLS=True
\`\`\`

### Telegram Bot
1. Создайте бота через @BotFather
2. Получите токен бота
3. Узнайте chat_id вашего чата
4. Добавьте в .env:
\`\`\`env
TELEGRAM_BOT_TOKEN=your-bot-token
TELEGRAM_CHAT_ID=your-chat-id
\`\`\`

## 🐳 Docker

\`\`\`bash
# Запуск всех сервисов
docker-compose up -d

# Применение миграций в контейнере
docker-compose exec web python manage.py migrate

# Загрузка данных
docker-compose exec web python manage.py load_initial_data
\`\`\`

## 📊 Админ панель

Доступна по адресу: `http://127.0.0.1:8000/admin/`

### Функции:
- ✅ Управление продуктами и их полями
- ✅ Просмотр и редактирование заявок
- ✅ Изменение статусов заявок
- ✅ Экспорт заявок в Excel
- ✅ Управление шаблонами уведомлений
- ✅ Просмотр логов уведомлений

## 🔄 Celery (фоновые задачи)

\`\`\`bash
# Запуск worker
celery -A config worker -l info

# Мониторинг задач
celery -A config flower
\`\`\`

## 📝 Структура проекта

\`\`\`
backend/
├── apps/
│   ├── core/           # Базовые модели и утилиты
│   ├── products/       # Страховые продукты
│   ├── applications/   # Заявки клиентов
│   ├── accounts/       # Профили администраторов
│   └── notifications/  # Email и Telegram уведомления
├── config/             # Настройки Django
├── templates/          # HTML шаблоны
├── static/            # Статические файлы
├── media/             # Загруженные файлы
└── logs/              # Логи приложения
\`\`\`

## 🧪 Тестирование

\`\`\`bash
# Запуск тестов
python manage.py test

# Проверка покрытия
coverage run --source='.' manage.py test
coverage report
\`\`\`

## 📞 Поддержка

- **Админка**: http://127.0.0.1:8000/admin/
- **API документация**: http://127.0.0.1:8000/api/
- **Логи**: `logs/django.log`

---

**Готово к тестированию!** 🎉

Создайте эту структуру в VS Code и запустите `./start.sh` для автоматической настройки.

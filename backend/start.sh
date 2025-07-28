#!/bin/bash

echo "🚀 Запуск страховой платформы..."

# Проверяем наличие .env файла
if [ ! -f .env ]; then
    echo "❌ Файл .env не найден! Создайте его на основе .env.example"
    exit 1
fi

# Создаем директории
mkdir -p logs media staticfiles

# Применяем миграции
echo "📦 Применение миграций..."
python manage.py makemigrations
python manage.py migrate

# Загружаем начальные данные
echo "📋 Загрузка начальных данных..."
python manage.py load_initial_data

# Создаем суперпользователя (если не существует)
echo "👤 Создание суперпользователя..."
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Суперпользователь создан: admin/admin123')
else:
    print('Суперпользователь уже существует')
"

# Собираем статические файлы
echo "🎨 Сборка статических файлов..."
python manage.py collectstatic --noinput

echo "✅ Настройка завершена!"
echo "🌐 Запуск сервера на http://127.0.0.1:8000"
echo "🔧 Админка доступна на http://127.0.0.1:8000/admin"
echo "📧 Логин: admin, Пароль: admin123"

# Запускаем сервер
python manage.py runserver

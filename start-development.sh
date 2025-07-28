#!/bin/bash

echo "🚀 Запуск полной разработки страховой платформы..."

# Проверяем что backend запущен
echo "🔍 Проверка backend..."
if curl -s http://127.0.0.1:8000/api/products/ > /dev/null; then
    echo "✅ Backend работает на http://127.0.0.1:8000"
else
    echo "❌ Backend не запущен! Запустите сначала backend:"
    echo "   cd backend && python manage.py runserver"
    exit 1
fi

# Переходим в frontend и запускаем
echo "🎨 Запуск frontend..."
cd frontend

if [ ! -d "node_modules" ]; then
    echo "📦 Установка зависимостей..."
    npm install
fi

echo "🌐 Запуск Next.js на http://localhost:3000"
npm run dev


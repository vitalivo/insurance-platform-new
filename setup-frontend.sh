#!/bin/bash

echo "🚀 Настройка Frontend для страховой платформы..."

# Создаем директорию frontend если её нет
if [ ! -d "frontend" ]; then
    mkdir frontend
    echo "✅ Создана директория frontend"
fi

cd frontend

# Инициализируем Next.js проект если его нет
if [ ! -f "package.json" ]; then
    echo "📦 Инициализация Next.js проекта..."
    npx create-next-app@latest . --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"
fi

# Устанавливаем дополнительные зависимости
echo "📦 Установка дополнительных пакетов..."
npm install @hookform/resolvers react-hook-form zod axios react-query lucide-react sonner class-variance-authority clsx tailwind-merge

# Устанавливаем shadcn/ui
echo "🎨 Настройка shadcn/ui..."
npx shadcn@latest init -y

# Устанавливаем нужные компоненты shadcn/ui
echo "🧩 Установка UI компонентов..."
npx shadcn@latest add button card input label select textarea toast

# Создаем .env.local файл
if [ ! -f ".env.local" ]; then
    echo "⚙️ Создание .env.local файла..."
    cat > .env.local << EOL
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000/api
NEXT_PUBLIC_SITE_URL=http://localhost:3000
EOL
    echo "✅ Создан .env.local файл"
fi

echo ""
echo "✅ Frontend настроен!"
echo ""
echo "🔗 Следующие шаги:"
echo "1. cd frontend"
echo "2. npm run dev"
echo "3. Открыть http://localhost:3000"
echo ""
echo "🎯 После запуска начинаем создавать компоненты!"

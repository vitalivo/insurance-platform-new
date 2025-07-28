## ТЕХНИЧЕСКИЙ СТЕК

### **Backend (Django)**

🔧 Core:
- Django 4.2+ 
- Django REST Framework
- PostgreSQL 16 (ваша готовая БД)
- Django CORS Headers

📧 Уведомления:
- Django Email Backend (SMTP)
- python-telegram-bot (интеграция с вашим ботом)
- Celery + Redis (для асинхронных задач)

📊 Дополнительно:
- openpyxl (экспорт в Excel)
- Pillow (обработка изображений)
- python-decouple (переменные окружения)

Frontend (React/TypeScript)

🎨 Core:
- React 18 + TypeScript
- Vite (быстрая сборка)
- React Router DOM

💅 Стилизация:
- Tailwind CSS (как на ваших скриншотах)
- Headless UI (компоненты)
- Lucide React (иконки)

📡 API & State:
- Axios (HTTP клиент)
- React Query/TanStack Query (кеширование)
- React Hook Form (формы)
- Zod (валидация)

Инфраструктура

🐳 Контейнеризация:
- Docker + Docker Compose
- Nginx (reverse proxy)

📨 Уведомления:
- SMTP сервер (ваша почта)
- Telegram Bot API
- Redis (очереди задач)

🗄️ База данных:
- PostgreSQL 16 (ваша готовая)
- Redis (кеш + очереди)

Структура проекта

insurance-platform-new/
├── backend/
│   ├── apps/
│   │   ├── __init__.py
│   │   ├── core/
│   │   ├── products/
│   │   ├── applications/
│   │   ├── accounts/
│   │   └── notifications/
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── celery.py
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env
│   ├── .env.example
│   ├── Dockerfile
│   ├── start.sh
│   ├── README.md
│   └── venv/
├── frontend/                 # Пустая папка для будущего
├── docker-compose.yml        # В корне проекта
└── Technical.md             # Ваша документация

Thought for 2s## ️ ОБНОВЛЕННЫЙ ТЕХНИЧЕСКИЙ СТЕК

### **Frontend (React/TypeScript) - Расширенный**

```plaintext
🎨 Core:
- React 18 + TypeScript
- Vite (быстрая сборка)
- React Router DOM

💅 Стилизация (отдельные файлы):
- CSS Modules + SCSS/SASS
- Tailwind CSS (утилиты)
- PostCSS (автопрефиксы)
- Clsx (условные классы)

📱 Адаптивность:
- CSS Grid + Flexbox
- Breakpoints: mobile (320px+), tablet (768px+), desktop (1024px+)
- Touch-friendly интерфейс
- Viewport meta настройки

🧩 Компонентная архитектура:
- Atomic Design (atoms, molecules, organisms)
- Storybook (документация компонентов)
- React.memo (оптимизация)
- Compound Components паттерн

🌍 Локализация (Россия):
- React-i18next (мультиязычность)
- Date-fns (русские даты)
- Русская типографика
- Локальные CDN (избегаем заблокированных)

📡 API & State:
- Axios (HTTP клиент)
- React Query/TanStack Query
- Zustand (легкий state manager)
- React Hook Form + Zod
```

### **Backend (Django) - Дополнения для России**

```plaintext
🔧 Core:
- Django 4.2+
- Django REST Framework
- PostgreSQL 16
- Django CORS Headers

🌍 Локализация:
- Django i18n (русский язык)
- Русские валидаторы (телефон, ИНН, СНИЛС)
- Timezone: Europe/Moscow
- Русские шаблоны email

📧 Уведомления (российские сервисы):
- Yandex SMTP / Mail.ru (вместо Gmail)
- python-telegram-bot
- Celery + Redis

📊 Российские интеграции:
- DaData API (адреса, ФИО)
- SMS.ru / SMSC.ru (SMS уведомления)
- Банковские API (если нужна оплата)
```

### **Структура Frontend (компонентная)**

```plaintext
frontend/src/
├── components/
│   ├── ui/                    # Атомы (Button, Input, Card)
│   │   ├── Button/
│   │   │   ├── Button.tsx
│   │   │   ├── Button.module.scss
│   │   │   └── index.ts
│   │   └── Input/
│   │       ├── Input.tsx
│   │       ├── Input.module.scss
│   │       └── index.ts
│   ├── forms/                 # Молекулы (формы)
│   │   ├── ApplicationForm/
│   │   │   ├── ApplicationForm.tsx
│   │   │   ├── ApplicationForm.module.scss
│   │   │   └── index.ts
│   └── layout/                # Организмы (Layout, Header)
│       ├── Header/
│       │   ├── Header.tsx
│       │   ├── Header.module.scss
│       │   ├── Header.mobile.scss
│       │   └── index.ts
├── pages/                     # Страницы
├── hooks/                     # Кастомные хуки
├── services/                  # API сервисы
├── styles/                    # Глобальные стили
│   ├── globals.scss
│   ├── variables.scss
│   ├── mixins.scss
│   └── breakpoints.scss
├── types/                     # TypeScript типы
├── utils/                     # Утилиты
└── locales/                   # Переводы
    ├── ru.json
    └── en.json
```


### **Российская специфика**

```plaintext
🇷🇺 Локализация:
- Русские форматы дат (ДД.ММ.ГГГГ)
- Российские номера телефонов (+7)
- Валидация ИНН, СНИЛС, паспорта
- Русская типографика (кавычки-ёлочки)

📱 Мобильная оптимизация:
- Touch targets 44px+
- Swipe жесты
- Виртуальная клавиатура
- iOS Safari quirks

🌐 CDN и сервисы:
- Yandex CDN (вместо Google)
- Российские шрифты
- Локальные иконки
```

### **Дополнительные инструменты**

```plaintext
🛠️ Development:
- Storybook (компоненты)
- ESLint + Prettier (код-стайл)
- Husky (git hooks)
- Chromatic (визуальное тестирование)

📱 Testing:
- Jest + React Testing Library
- Cypress (E2E)
- Responsive design testing
- Cross-browser testing

🚀 Build & Deploy:
- Vite (сборка)
- Docker multi-stage
- Nginx gzip
- PWA возможности
```

## Ключевые преимущества обновленного стека:

1. **Полная компонентность** - каждый компонент изолирован
2. **Отдельные стили** - maintainable CSS/SCSS модули
3. **Адаптивность** - mobile-first подход
4. **Российская локализация** - все под местный рынок
5. **Производительность** - оптимизация для мобильных сетей
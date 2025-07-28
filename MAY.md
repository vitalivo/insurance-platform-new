frontend/
├── app/                    # Next.js App Router
│   ├── globals.css        # Глобальные стили
│   ├── layout.tsx         # Основной layout
│   ├── page.tsx           # Главная страница
│   ├── providers.tsx      # React Query провайдеры
│   ├── products/          # Страницы продуктов
│   ├── track/             # Отслеживание заявок
│   ├── admin/             # Админ панель
│   ├── contacts/          # Контакты
│   ├── partners/          # Партнеры
│   └── agent/             # Агент
├── components/             # React компоненты
│   ├── layout/            # Header, Footer
│   ├── sections/          # Секции страниц
│   └── ui/                # UI компоненты
├── lib/                   # Утилиты
│   ├── api.ts            # API клиент
│   └── icons.ts          # Иконки
├── hooks/                 # Custom hooks
├── package.json          # Зависимости
├── next.config.js        # Конфигурация Next.js
├── tailwind.config.ts    # Конфигурация Tailwind
└── .env.local            # Переменные окружения
import Link from "next/link"
import { Shield, Phone, Mail, MapPin } from "lucide-react"

export function Footer() {
  return (
    <footer className="bg-gray-900 text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {/* Logo and description */}
          <div className="col-span-1 md:col-span-2">
            <div className="flex items-center space-x-2 mb-4">
              <div className="bg-blue-600 p-2 rounded-lg">
                <Shield className="h-6 w-6 text-white" />
              </div>
              <div>
                <span className="text-xl font-bold">СП</span>
                <span className="text-sm text-gray-300 ml-1">Страховая платформа</span>
              </div>
            </div>
            <p className="text-gray-300 mb-4">
              Быстрое и удобное оформление страховых полисов онлайн. Надежная защита для вас и вашего имущества.
            </p>
            <div className="space-y-2">
              <div className="flex items-center space-x-2">
                <Phone className="h-4 w-4 text-blue-400" />
                <span className="text-gray-300">8 (800) 123-45-67</span>
              </div>
              <div className="flex items-center space-x-2">
                <Mail className="h-4 w-4 text-blue-400" />
                <span className="text-gray-300">info@insurance-platform.ru</span>
              </div>
              <div className="flex items-center space-x-2">
                <MapPin className="h-4 w-4 text-blue-400" />
                <span className="text-gray-300">Москва, ул. Примерная, д. 123</span>
              </div>
            </div>
          </div>

          {/* Quick links */}
          <div>
            <h3 className="text-lg font-semibold mb-4">Быстрые ссылки</h3>
            <ul className="space-y-2">
              <li>
                <Link href="/" className="text-gray-300 hover:text-white transition-colors duration-200">
                  Главная
                </Link>
              </li>
              <li>
                <Link href="/track" className="text-gray-300 hover:text-white transition-colors duration-200">
                  Отследить заявку
                </Link>
              </li>
              <li>
                <Link href="/contacts" className="text-gray-300 hover:text-white transition-colors duration-200">
                  Контакты
                </Link>
              </li>
              <li>
                <Link href="/partners" className="text-gray-300 hover:text-white transition-colors duration-200">
                  Партнеры
                </Link>
              </li>
            </ul>
          </div>

          {/* Legal */}
          <div>
            <h3 className="text-lg font-semibold mb-4">Правовая информация</h3>
            <ul className="space-y-2">
              <li>
                <Link href="/privacy" className="text-gray-300 hover:text-white transition-colors duration-200">
                  Политика конфиденциальности
                </Link>
              </li>
              <li>
                <Link href="/terms" className="text-gray-300 hover:text-white transition-colors duration-200">
                  Условия использования
                </Link>
              </li>
              <li>
                <Link href="/agent" className="text-gray-300 hover:text-white transition-colors duration-200">
                  Об агенте
                </Link>
              </li>
            </ul>
          </div>
        </div>

        <div className="border-t border-gray-800 mt-8 pt-8 text-center">
          <p className="text-gray-400">© 2025 Страховая платформа. Все права защищены.</p>
        </div>
      </div>
    </footer>
  )
}


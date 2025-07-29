import Link from "next/link"
import { Shield, Phone, Mail, MapPin, Clock, Award } from "lucide-react"

export function Footer() {
  return (
    <footer className="bg-gray-900 text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {/* Компания */}
          <div className="col-span-1 md:col-span-2">
            <div className="flex items-center space-x-2 mb-6">
              <div className="bg-blue-600 p-2 rounded-lg">
                <Shield className="h-6 w-6 text-white" />
              </div>
              <div>
                <span className="text-xl font-bold">СтрахПлатформа</span>
                <div className="text-sm text-gray-300">Надежная защита</div>
              </div>
            </div>

            <p className="text-gray-300 mb-6 leading-relaxed">
              Современная страховая платформа для быстрого и удобного оформления полисов онлайн. Работаем с ведущими
              страховыми компаниями России.
            </p>

            {/* Преимущества */}
            <div className="grid grid-cols-2 gap-4 mb-6">
              <div className="flex items-center space-x-2">
                <Clock className="h-4 w-4 text-blue-400" />
                <span className="text-sm text-gray-300">Работаем 24/7</span>
              </div>
              <div className="flex items-center space-x-2">
                <Award className="h-4 w-4 text-blue-400" />
                <span className="text-sm text-gray-300">Лицензированы</span>
              </div>
            </div>
          </div>

          {/* Контакты */}
          <div>
            <h3 className="text-lg font-semibold mb-4 text-white">Контакты</h3>
            <div className="space-y-3">
              <div className="flex items-start space-x-3">
                <Phone className="h-4 w-4 text-blue-400 mt-0.5 flex-shrink-0" />
                <div>
                  <Link
                    href="tel:+78001234567"
                    className="text-gray-300 hover:text-white transition-colors duration-200"
                  >
                    8 (800) 123-45-67
                  </Link>
                  <div className="text-xs text-gray-400">Бесплатно по России</div>
                </div>
              </div>

              <div className="flex items-start space-x-3">
                <Mail className="h-4 w-4 text-blue-400 mt-0.5 flex-shrink-0" />
                <div>
                  <Link
                    href="mailto:info@strah-platform.ru"
                    className="text-gray-300 hover:text-white transition-colors duration-200"
                  >
                    info@strah-platform.ru
                  </Link>
                  <div className="text-xs text-gray-400">Техподдержка</div>
                </div>
              </div>

              <div className="flex items-start space-x-3">
                <MapPin className="h-4 w-4 text-blue-400 mt-0.5 flex-shrink-0" />
                <div>
                  <span className="text-gray-300">Москва, ул. Тверская, 15</span>
                  <div className="text-xs text-gray-400">Офис продаж</div>
                </div>
              </div>
            </div>
          </div>

          {/* Информация */}
          <div>
            <h3 className="text-lg font-semibold mb-4 text-white">Информация</h3>
            <ul className="space-y-2">
              <li>
                <span className="text-gray-300">О компании</span>
              </li>
              <li>
                <span className="text-gray-300">Лицензии</span>
              </li>
              <li>
                <span className="text-gray-300">Партнеры</span>
              </li>
              <li>
                <span className="text-gray-300">Вакансии</span>
              </li>
              <li>
                <span className="text-gray-300">Политика конфиденциальности</span>
              </li>
            </ul>
          </div>
        </div>

        {/* Нижняя часть */}
        <div className="border-t border-gray-800 mt-8 pt-8">
          <div className="flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0">
            <div className="text-gray-400 text-sm">© 2025 СтрахПлатформа. Все права защищены.</div>

            <div className="flex items-center space-x-6 text-sm text-gray-400">
              <span>Лицензия ЦБ РФ № 12345</span>
              <span>•</span>
              <span>Член РСА</span>
            </div>
          </div>
        </div>
      </div>
    </footer>
  )
}



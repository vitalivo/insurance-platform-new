import Link from "next/link"
import { ArrowRight, Shield, Clock, Award } from "lucide-react"

export function HeroSection() {
  return (
    <section className="relative bg-gradient-to-br from-blue-50 via-white to-blue-50 pt-16 pb-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          {/* Badge */}
          <div className="inline-flex items-center space-x-2 bg-blue-100 text-blue-800 px-4 py-2 rounded-full text-sm font-medium mb-8">
            <Shield className="h-4 w-4" />
            <span>Надежная страховая защита</span>
          </div>

          {/* Main heading */}
          <h1 className="text-4xl md:text-6xl font-bold text-gray-900 mb-6">Страховая платформа</h1>

          <p className="text-xl md:text-2xl text-gray-600 mb-8 max-w-3xl mx-auto">
            Быстрое и удобное оформление страховых полисов онлайн
          </p>

          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center mb-12">
            <Link href="#products" className="btn-primary text-lg px-8 py-3 flex items-center space-x-2">
              <span>Выбрать страховку</span>
              <ArrowRight className="h-5 w-5" />
            </Link>
            <Link href="/track" className="btn-secondary text-lg px-8 py-3">
              Отследить заявку
            </Link>
          </div>

          {/* Quick stats */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl mx-auto">
            <div className="flex flex-col items-center">
              <div className="bg-blue-100 p-3 rounded-full mb-3">
                <Clock className="h-6 w-6 text-blue-600" />
              </div>
              <div className="text-2xl font-bold text-gray-900">5 мин</div>
              <div className="text-gray-600">Оформление заявки</div>
            </div>
            <div className="flex flex-col items-center">
              <div className="bg-blue-100 p-3 rounded-full mb-3">
                <Shield className="h-6 w-6 text-blue-600" />
              </div>
              <div className="text-2xl font-bold text-gray-900">100%</div>
              <div className="text-gray-600">Защита данных</div>
            </div>
            <div className="flex flex-col items-center">
              <div className="bg-blue-100 p-3 rounded-full mb-3">
                <Award className="h-6 w-6 text-blue-600" />
              </div>
              <div className="text-2xl font-bold text-gray-900">24/7</div>
              <div className="text-gray-600">Поддержка клиентов</div>
            </div>
          </div>
        </div>
      </div>

      {/* Background decoration */}
      <div className="absolute inset-0 -z-10 overflow-hidden">
        <div className="absolute -top-40 -right-32 w-80 h-80 bg-blue-200 rounded-full opacity-20 blur-3xl"></div>
        <div className="absolute -bottom-40 -left-32 w-80 h-80 bg-blue-300 rounded-full opacity-20 blur-3xl"></div>
      </div>
    </section>
  )
}

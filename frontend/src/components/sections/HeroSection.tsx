import Link from "next/link"
import { ArrowRight, Shield, Clock, Award, CheckCircle, Phone } from "lucide-react"

export function HeroSection() {
  return (
    <section className="relative bg-gradient-to-br from-blue-50 via-white to-blue-50 pt-20 pb-24">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          {/* Badge */}
          <div className="inline-flex items-center space-x-2 bg-blue-100 text-blue-800 px-4 py-2 rounded-full text-sm font-medium mb-8 animate-fade-in">
            <Shield className="h-4 w-4" />
            <span>Надежная страховая защита с 2020 года</span>
          </div>

          {/* Main heading */}
          <h1 className="text-4xl md:text-6xl font-bold text-gray-900 mb-6 leading-tight">
            Страховая платформа
            <span className="block text-blue-600">нового поколения</span>
          </h1>

          <p className="text-xl md:text-2xl text-gray-600 mb-8 max-w-4xl mx-auto leading-relaxed">
            Быстрое и удобное оформление страховых полисов онлайн. Работаем с ведущими страховыми компаниями России.
          </p>

          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center mb-12">
            <Link
              href="#products"
              className="btn-primary text-lg px-8 py-4 flex items-center space-x-2 shadow-lg hover:shadow-xl transition-all duration-200"
            >
              <span>Выбрать страховку</span>
              <ArrowRight className="h-5 w-5" />
            </Link>
            <Link href="tel:+78001234567" className="btn-secondary text-lg px-8 py-4 flex items-center space-x-2">
              <Phone className="h-5 w-5" />
              <span>Получить консультацию</span>
            </Link>
          </div>

          {/* Преимущества */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">
            <div className="flex flex-col items-center p-6 bg-white rounded-xl shadow-sm border border-gray-100">
              <div className="bg-blue-100 p-4 rounded-full mb-4">
                <Clock className="h-8 w-8 text-blue-600" />
              </div>
              <div className="text-3xl font-bold text-gray-900 mb-2">5 мин</div>
              <div className="text-gray-600 text-center">Оформление полиса онлайн</div>
            </div>

            <div className="flex flex-col items-center p-6 bg-white rounded-xl shadow-sm border border-gray-100">
              <div className="bg-blue-100 p-4 rounded-full mb-4">
                <Shield className="h-8 w-8 text-blue-600" />
              </div>
              <div className="text-3xl font-bold text-gray-900 mb-2">100%</div>
              <div className="text-gray-600 text-center">Защита персональных данных</div>
            </div>

            <div className="flex flex-col items-center p-6 bg-white rounded-xl shadow-sm border border-gray-100">
              <div className="bg-blue-100 p-4 rounded-full mb-4">
                <Award className="h-8 w-8 text-blue-600" />
              </div>
              <div className="text-3xl font-bold text-gray-900 mb-2">24/7</div>
              <div className="text-gray-600 text-center">Поддержка клиентов</div>
            </div>
          </div>

          {/* Дополнительная информация */}
          <div className="mt-12 flex flex-wrap justify-center items-center gap-6 text-sm text-gray-500">
            <div className="flex items-center space-x-2">
              <CheckCircle className="h-4 w-4 text-green-500" />
              <span>Лицензия ЦБ РФ</span>
            </div>
            <div className="flex items-center space-x-2">
              <CheckCircle className="h-4 w-4 text-green-500" />
              <span>Член РСА</span>
            </div>
            <div className="flex items-center space-x-2">
              <CheckCircle className="h-4 w-4 text-green-500" />
              <span>Более 50 000 клиентов</span>
            </div>
          </div>
        </div>
      </div>

      {/* Background decoration */}
      <div className="absolute inset-0 -z-10 overflow-hidden">
        <div className="absolute -top-40 -right-32 w-80 h-80 bg-blue-200 rounded-full opacity-20 blur-3xl animate-pulse-slow"></div>
        <div className="absolute -bottom-40 -left-32 w-80 h-80 bg-blue-300 rounded-full opacity-20 blur-3xl animate-pulse-slow"></div>
      </div>
    </section>
  )
}


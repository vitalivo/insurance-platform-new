import { Zap, Lock, Headphones, Users, FileCheck, CreditCard } from "lucide-react"

export function FeaturesSection() {
  const features = [
    {
      icon: Zap,
      title: "Быстро",
      description: "Оформление заявки за 5 минут без походов в офис",
      color: "bg-yellow-100 text-yellow-600",
    },
    {
      icon: Lock,
      title: "Безопасно",
      description: "Защита данных по стандартам банковской безопасности",
      color: "bg-green-100 text-green-600",
    },
    {
      icon: Headphones,
      title: "Поддержка 24/7",
      description: "Консультации и помощь в любое время суток",
      color: "bg-blue-100 text-blue-600",
    },
    {
      icon: Users,
      title: "Опытные агенты",
      description: "Профессиональные консультанты с опытом более 5 лет",
      color: "bg-purple-100 text-purple-600",
    },
    {
      icon: FileCheck,
      title: "Простое оформление",
      description: "Минимум документов, максимум удобства",
      color: "bg-indigo-100 text-indigo-600",
    },
    {
      icon: CreditCard,
      title: "Удобная оплата",
      description: "Оплата картой, переводом или в рассрочку",
      color: "bg-pink-100 text-pink-600",
    },
  ]

  return (
    <section id="features" className="py-20 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">Почему выбирают нас?</h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Мы создали платформу, которая делает страхование простым, быстрым и надежным
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <div
              key={index}
              className="bg-white p-8 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-all duration-200 group"
            >
              <div
                className={`w-14 h-14 rounded-xl ${feature.color} flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-200`}
              >
                <feature.icon className="h-7 w-7" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-3">{feature.title}</h3>
              <p className="text-gray-600 leading-relaxed">{feature.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}


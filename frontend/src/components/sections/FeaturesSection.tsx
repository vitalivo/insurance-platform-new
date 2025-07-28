import { Zap, Lock, Headphones } from "lucide-react"

export function FeaturesSection() {
  const features = [
    {
      icon: Zap,
      title: "Быстро",
      description: "Оформление заявки за 5 минут",
    },
    {
      icon: Lock,
      title: "Безопасно",
      description: "Защита персональных данных",
    },
    {
      icon: Headphones,
      title: "Поддержка",
      description: "Консультации 24/7",
    },
  ]

  return (
    <section className="py-16 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">Почему выбирают нас?</h2>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <div key={index} className="text-center">
              <div className="bg-blue-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <feature.icon className="h-8 w-8 text-blue-600" />
              </div>
              <h3 className="text-xl font-bold text-gray-900 mb-2">{feature.title}</h3>
              <p className="text-gray-600">{feature.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}


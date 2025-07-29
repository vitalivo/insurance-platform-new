import { TrendingUp, Users, Award, Clock } from "lucide-react"

export function StatsSection() {
  const stats = [
    {
      icon: Users,
      value: "50,000+",
      label: "Довольных клиентов",
      description: "Выбрали нашу платформу",
    },
    {
      icon: Award,
      value: "99.8%",
      label: "Положительных отзывов",
      description: "От наших клиентов",
    },
    {
      icon: Clock,
      value: "24/7",
      label: "Поддержка клиентов",
      description: "Всегда готовы помочь",
    },
    {
      icon: TrendingUp,
      value: "5 лет",
      label: "На рынке страхования",
      description: "Опыт и надежность",
    },
  ]

  return (
    <section id="about" className="py-20 bg-blue-600">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold text-white mb-4">Нам доверяют</h2>
          <p className="text-xl text-blue-100 max-w-3xl mx-auto">
            Цифры, которые говорят о нашей надежности и профессионализме
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {stats.map((stat, index) => (
            <div key={index} className="text-center">
              <div className="bg-blue-500 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <stat.icon className="h-8 w-8 text-white" />
              </div>
              <div className="text-3xl font-bold text-white mb-2">{stat.value}</div>
              <div className="text-lg font-semibold text-blue-100 mb-1">{stat.label}</div>
              <div className="text-sm text-blue-200">{stat.description}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

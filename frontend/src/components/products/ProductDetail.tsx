"use client"

import { useState } from "react"
import type { Product } from "@/lib/api"
import { getProductIcon } from "@/lib/icons"
import { ApplicationForm } from "@/components/forms/ApplicationForm"
import { CheckCircle, Clock, DollarSign } from "lucide-react"

interface ProductDetailProps {
  product: Product
}

export function ProductDetail({ product }: ProductDetailProps) {
  const [showForm, setShowForm] = useState(false)
  const Icon = getProductIcon(product.icon)

  // Безопасный парсинг benefits из JSON строки
  const getBenefits = (benefitsData: string[] | string | null | undefined): string[] => {
    if (!benefitsData) return []

    // Если уже массив
    if (Array.isArray(benefitsData)) {
      return benefitsData
    }

    // Если строка, пытаемся распарсить JSON
    if (typeof benefitsData === "string") {
      try {
        const parsed = JSON.parse(benefitsData)
        return Array.isArray(parsed) ? parsed : []
      } catch (error) {
        console.warn("Ошибка парсинга benefits:", error)
        return []
      }
    }

    return []
  }

  const benefits = getBenefits(product.benefits)

  return (
    <div className="bg-white rounded-xl shadow-lg overflow-hidden">
      {/* Hero секция продукта */}
      <div className="bg-gradient-to-r from-blue-600 to-blue-700 text-white p-8 md:p-12">
        <div className="max-w-4xl mx-auto">
          <div className="flex items-center space-x-4 mb-6">
            <div
              className="w-16 h-16 rounded-full flex items-center justify-center"
              style={{ backgroundColor: product.icon_background_color || "rgba(255,255,255,0.2)" }}
            >
              <Icon className="h-8 w-8 text-white" />
            </div>
            <div>
              <h1 className="text-3xl md:text-4xl font-bold">{product.name}</h1>
              <p className="text-blue-100 text-lg">{product.short_description}</p>
            </div>
          </div>

          {/* Дополнительная информация */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-8">
            {product.price_range && (
              <div className="flex items-center space-x-3">
                <DollarSign className="h-6 w-6 text-blue-200" />
                <div>
                  <div className="text-sm text-blue-200">Стоимость</div>
                  <div className="font-semibold">{product.price_range}</div>
                </div>
              </div>
            )}

            {product.processing_time && (
              <div className="flex items-center space-x-3">
                <Clock className="h-6 w-6 text-blue-200" />
                <div>
                  <div className="text-sm text-blue-200">Время оформления</div>
                  <div className="font-semibold">{product.processing_time}</div>
                </div>
              </div>
            )}

            <div className="flex items-center space-x-3">
              <CheckCircle className="h-6 w-6 text-green-300" />
              <div>
                <div className="text-sm text-blue-200">Статус</div>
                <div className="font-semibold">Доступно онлайн</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="p-8 md:p-12">
        <div className="max-w-4xl mx-auto">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
            {/* Левая колонка - описание и преимущества */}
            <div className="space-y-8">
              {/* Описание */}
              <div>
                <h2 className="text-2xl font-bold text-gray-900 mb-4">Описание продукта</h2>
                <div
                  className="text-gray-600 leading-relaxed prose prose-blue max-w-none"
                  dangerouslySetInnerHTML={{ __html: product.description || "" }}
                />
              </div>

              {/* Преимущества */}
              {benefits.length > 0 && (
                <div>
                  <h3 className="text-xl font-bold text-gray-900 mb-4">Преимущества</h3>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    {benefits.map((benefit: string, index: number) => (
                      <div key={index} className="flex items-center space-x-3">
                        <CheckCircle className="h-5 w-5 text-green-500 flex-shrink-0" />
                        <span className="text-gray-700">{benefit}</span>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>

            {/* Правая колонка - форма заявки */}
            <div className="lg:sticky lg:top-8">
              <div className="bg-gray-50 rounded-xl p-6">
                <h3 className="text-xl font-bold text-gray-900 mb-4">Оформить заявку</h3>
                <p className="text-gray-600 mb-6">
                  Заполните форму, и наш специалист свяжется с вами для оформления полиса
                </p>

                {!showForm ? (
                  <button onClick={() => setShowForm(true)} className="btn-primary w-full py-3 text-lg">
                    {product.button_text || "Оформить полис"}
                  </button>
                ) : (
                  <ApplicationForm
                    product={product}
                    onSuccess={() => {
                      setShowForm(false)
                      // Можно добавить уведомление об успехе
                    }}
                    onCancel={() => setShowForm(false)}
                  />
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

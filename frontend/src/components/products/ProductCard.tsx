import Link from "next/link"
import type { Product } from "@/lib/api"
import { getProductIcon } from "@/lib/icons"
import { cn } from "@/lib/utils"

interface ProductCardProps {
  product: Product
  className?: string
}

export function ProductCard({ product, className }: ProductCardProps) {
  const Icon = getProductIcon(product.icon)

  // Используем цвета из админки или значения по умолчанию
  const cardBgColor = product.card_background_color || "#ffffff"
  const iconBgColor = product.icon_background_color || "#dbeafe"
  const buttonText = product.button_text || "Оформить полис"

  return (
    <div
      className={cn("card group hover:scale-105 transition-transform duration-200", className)}
      style={{ backgroundColor: cardBgColor }}
    >
      <div className="text-center">
        <div
          className="w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-200"
          style={{ backgroundColor: iconBgColor }}
        >
          <Icon className="h-8 w-8 text-blue-600" />
        </div>

        <h3 className="text-xl font-bold text-gray-900 mb-3">{product.name}</h3>

        <p className="text-gray-600 mb-4 text-sm leading-relaxed">{product.short_description}</p>

        {/* Дополнительная информация из админки */}
        <div className="space-y-2 mb-6">
          {product.price_range && <p className="text-sm text-blue-600 font-medium">{product.price_range}</p>}

          {product.processing_time && <p className="text-xs text-gray-500">Оформление: {product.processing_time}</p>}
        </div>

        <Link href={`/products/${product.slug}`} className="btn-primary w-full inline-block text-center">
          {buttonText}
        </Link>
      </div>
    </div>
  )
}

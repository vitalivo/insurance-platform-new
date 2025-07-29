import Link from "next/link"
import type { Product } from "@/lib/api"
import { getProductIcon } from "@/lib/icons"

interface ProductCardProps {
  product: Product
}

export function ProductCard({ product }: ProductCardProps) {
  const Icon = getProductIcon(product.icon)

  return (
    <div className="card group hover:scale-105 transition-transform duration-200">
      <div className="text-center">
        <div className="bg-blue-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:bg-blue-200 transition-colors duration-200">
          <Icon className="h-8 w-8 text-blue-600" />
        </div>

        <h3 className="text-xl font-bold text-gray-900 mb-3">{product.name}</h3>

        <p className="text-gray-600 mb-6 text-sm leading-relaxed">{product.short_description}</p>

        <Link href={`/products/${product.slug}`} className="btn-primary w-full inline-block text-center">
          Оформить полис
        </Link>
      </div>
    </div>
  )
}

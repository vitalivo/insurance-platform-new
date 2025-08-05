"use client"

import { useProducts } from "@/hooks/useProducts"
import { ProductCard } from "@/components/products/ProductCard"
import { LoadingSpinner } from "@/components/ui/LoadingSpinner"

export function ProductGrid() {
  const { data: products, isLoading, error } = useProducts()

  if (isLoading) {
    return (
      <div className="flex justify-center py-12">
        <LoadingSpinner size="lg" />
      </div>
    )
  }

  if (error) {
    return (
      <div className="text-center py-12">
        <p className="text-red-600 text-lg">Ошибка загрузки продуктов: {error.message}</p>
        <button onClick={() => window.location.reload()} className="btn-primary mt-4">
          Попробовать снова
        </button>
      </div>
    )
  }

  if (!products || products.length === 0) {
    return (
      <div className="text-center py-12">
        <p className="text-gray-600 text-lg">Продукты не найдены</p>
      </div>
    )
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  )
}

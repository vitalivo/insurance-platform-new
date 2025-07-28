"use client"

import { useProducts } from "@/hooks/useProducts"
import { ProductCard } from "@/components/ui/ProductCard"
import { LoadingSpinner } from "@/components/ui/LoadingSpinner"

export function ProductsSection() {
  const { data: products, isLoading, error } = useProducts()

  console.log("Products data:", products)

  if (isLoading) {
    return (
      <section id="products" className="py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">Наши страховые продукты</h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Выберите подходящий вид страхования и оформите полис онлайн
            </p>
          </div>
          <div className="flex justify-center">
            <LoadingSpinner size="lg" />
          </div>
        </div>
      </section>
    )
  }

  if (error) {
    console.error("Products error:", error)
    return (
      <section id="products" className="py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <p className="text-red-600">Ошибка загрузки продуктов: {error.message}</p>
          </div>
        </div>
      </section>
    )
  }

  if (!products || !Array.isArray(products)) {
    console.error("Products is not an array:", products)
    return (
      <section id="products" className="py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <p className="text-red-600">Неверный формат данных продуктов</p>
          </div>
        </div>
      </section>
    )
  }

  return (
    <section id="products" style={{ padding: "4rem 0", backgroundColor: "white" }}>
      <div style={{ maxWidth: "80rem", margin: "0 auto", padding: "0 1rem" }}>
        <div style={{ textAlign: "center", marginBottom: "3rem" }}>
          <h2 style={{ fontSize: "2.5rem", fontWeight: "bold", color: "#111827", marginBottom: "1rem" }}>
            Наши страховые продукты
          </h2>
          <p style={{ fontSize: "1.25rem", color: "#6b7280", maxWidth: "48rem", margin: "0 auto" }}>
            Выберите подходящий вид страхования и оформите полис онлайн
          </p>
        </div>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))",
            gap: "2rem",
          }}
        >
          {products.map((product) => (
            <ProductCard key={product.id} product={product} />
          ))}
        </div>
      </div>
    </section>
  )
}

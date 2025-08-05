import type { Metadata } from "next"
import { ProductGrid } from "@/components/products/ProductGrid"
import { Breadcrumbs } from "@/components/ui/Breadcrumbs"

export const metadata: Metadata = {
  title: "Страховые продукты | СтрахПлатформа",
  description:
    "Выберите подходящий вид страхования и оформите полис онлайн. ОСАГО, КАСКО, страхование недвижимости и другие продукты.",
}

export default function ProductsPage() {
  const breadcrumbs = [
    { label: "Главная", href: "/" },
    { label: "Продукты", href: "/products" },
  ]

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <Breadcrumbs items={breadcrumbs} />

        <div className="mt-8">
          <div className="text-center mb-12">
            <h1 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">Наши страховые продукты</h1>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Выберите подходящий вид страхования и оформите полис онлайн. Быстро, надежно и выгодно.
            </p>
          </div>

          <ProductGrid />
        </div>
      </div>
    </div>
  )
}

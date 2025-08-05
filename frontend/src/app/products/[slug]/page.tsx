import type { Metadata } from "next"
import { notFound } from "next/navigation"
import { ProductDetail } from "@/components/products/ProductDetail"
import { Breadcrumbs } from "@/components/ui/Breadcrumbs"
import { productsApi } from "@/lib/api"

interface ProductPageProps {
  params: Promise<{ slug: string }>
}

export async function generateMetadata({ params }: ProductPageProps): Promise<Metadata> {
  const { slug } = await params

  try {
    const response = await productsApi.getSEO(slug)
    const seoData = response.data

    return {
      title: seoData.meta_title || `${seoData.name} | СтрахПлатформа`,
      description: seoData.meta_description || seoData.description,
    }
  } catch (error) {
    return {
      title: "Продукт не найден | СтрахПлатформа",
      description: "Запрашиваемый страховой продукт не найден.",
    }
  }
}

export default async function ProductPage({ params }: ProductPageProps) {
  const { slug } = await params
  let product

  try {
    const response = await productsApi.getBySlug(slug)
    product = response.data
  } catch (error) {
    notFound()
  }

  const breadcrumbs = [
    { label: "Главная", href: "/" },
    { label: "Продукты", href: "/products" },
    { label: product.name, href: `/products/${product.slug}` },
  ]

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <Breadcrumbs items={breadcrumbs} />

        <div className="mt-8">
          <ProductDetail product={product} />
        </div>
      </div>
    </div>
  )
}

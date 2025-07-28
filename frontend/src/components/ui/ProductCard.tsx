import Link from "next/link"
import type { Product } from "@/lib/api"
import { getProductIcon } from "@/lib/icons"

interface ProductCardProps {
  product: Product
}

export function ProductCard({ product }: ProductCardProps) {
  const Icon = getProductIcon(product.icon)

  return (
    <div className="card" style={{ textAlign: "center", transform: "scale(1)", transition: "transform 0.2s" }}>
      <div
        style={{
          backgroundColor: "#dbeafe",
          width: "4rem",
          height: "4rem",
          borderRadius: "50%",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          margin: "0 auto 1rem",
        }}
      >
        <Icon style={{ width: "2rem", height: "2rem", color: "#2563eb" }} />
      </div>

      <h3 style={{ fontSize: "1.25rem", fontWeight: "bold", color: "#111827", marginBottom: "0.5rem" }}>
        {product.name}
      </h3>

      <p style={{ color: "#6b7280", marginBottom: "1.5rem", fontSize: "0.875rem", lineHeight: "1.5" }}>
        {product.short_description}
      </p>

      <Link href={`/products/${product.slug}`} className="btn-primary" style={{ width: "100%" }}>
        Оформить
      </Link>
    </div>
  )
}

import { useQuery } from "@tanstack/react-query"
import { productsApi, type Product } from "@/lib/api"

export function useProducts() {
  return useQuery<Product[], Error>({
    queryKey: ["products"],
    queryFn: async () => {
      console.log("Fetching products...")
      const response = await productsApi.getAll()
      console.log("API Response:", response.data)
      return response.data
    },
  })
}

export function useProduct(slug: string) {
  return useQuery<Product, Error>({
    queryKey: ["product", slug],
    queryFn: async () => {
      const response = await productsApi.getBySlug(slug)
      return response.data
    },
    enabled: !!slug,
  })
}

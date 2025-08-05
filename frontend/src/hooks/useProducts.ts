"use client"

import { useQuery } from "@tanstack/react-query"
import { productsApi } from "@/lib/api"

export function useProducts() {
  return useQuery({
    queryKey: ["products"],
    queryFn: async () => {
      const response = await productsApi.getAll()
      return response.data
    },
    staleTime: 5 * 60 * 1000, // 5 минут
  })
}

export function useProduct(slug: string) {
  return useQuery({
    queryKey: ["product", slug],
    queryFn: async () => {
      const response = await productsApi.getBySlug(slug)
      return response.data
    },
    enabled: !!slug,
    staleTime: 5 * 60 * 1000, // 5 минут
  })
}

export function useFeaturedProducts() {
  return useQuery({
    queryKey: ["featured-products"],
    queryFn: async () => {
      const response = await productsApi.getFeatured()
      return response.data
    },
    staleTime: 5 * 60 * 1000, // 5 минут
  })
}

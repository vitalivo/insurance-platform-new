import type React from "react"
import type { Metadata, Viewport } from "next"
import { Inter } from "next/font/google"
import "./globals.css"
import { Providers } from "./providers"
import { Header } from "@/components/layout/Header"
import { Footer } from "@/components/layout/Footer"
import { Toaster } from "sonner"

const inter = Inter({ subsets: ["latin", "cyrillic"] })

export const metadata: Metadata = {
  title: "Страховая платформа - Быстрое оформление страховых полисов",
  description:
    "Быстрое и удобное оформление страховых полисов онлайн. ОСАГО, КАСКО, страхование недвижимости, от несчастных случаев и многое другое.",
  keywords: "страхование, ОСАГО, КАСКО, недвижимость, несчастный случай, ипотека, клещ",
  authors: [{ name: "Insurance Platform Team" }],
  robots: "index, follow",
  openGraph: {
    title: "Страховая платформа",
    description: "Быстрое и удобное оформление страховых полисов онлайн",
    type: "website",
    locale: "ru_RU",
  },
}

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="ru">
      <body className={inter.className}>
        <Providers>
          <div className="min-h-screen flex flex-col">
            <Header />
            <main className="flex-1">{children}</main>
            <Footer />
          </div>
          <Toaster position="top-right" richColors closeButton duration={5000} />
        </Providers>
      </body>
    </html>
  )
}

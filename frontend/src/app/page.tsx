import { HeroSection } from "@/components/sections/HeroSection"
import { ProductsSection } from "@/components/sections/ProductsSection"
import { FeaturesSection } from "@/components/sections/FeaturesSection"
import { StatsSection } from "@/components/sections/StatsSection"

export default function HomePage() {
  return (
    <div className="min-h-screen">
      <HeroSection />
      <ProductsSection />
      <FeaturesSection />
      <StatsSection />
    </div>
  )
}

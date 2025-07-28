import { HeroSection } from "@/components/sections/HeroSection"
import { ProductsSection } from "@/components/sections/ProductsSection"
import { FeaturesSection } from "@/components/sections/FeaturesSection"

export default function HomePage() {
  return (
    <div className="space-y-16 pb-16">
      <HeroSection />
      <ProductsSection />
      <FeaturesSection />
    </div>
  )
}

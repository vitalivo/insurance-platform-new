import Link from "next/link"
import { ChevronRight } from "lucide-react"

interface BreadcrumbItem {
  label: string
  href: string
}

interface BreadcrumbsProps {
  items: BreadcrumbItem[]
}

export function Breadcrumbs({ items }: BreadcrumbsProps) {
  return (
    <nav className="flex items-center space-x-2 text-sm text-gray-600">
      {items.map((item, index) => (
        <div key={item.href} className="flex items-center space-x-2">
          {index > 0 && <ChevronRight className="h-4 w-4" />}

          {index === items.length - 1 ? (
            <span className="text-gray-900 font-medium">{item.label}</span>
          ) : (
            <Link href={item.href} className="hover:text-blue-600 transition-colors duration-200">
              {item.label}
            </Link>
          )}
        </div>
      ))}
    </nav>
  )
}

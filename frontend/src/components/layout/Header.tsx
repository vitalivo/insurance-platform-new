"use client"

import Link from "next/link"
import { useState } from "react"
import { Menu, X, Shield, Phone, User } from "lucide-react"

export function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  // Обновленная навигация с правильной ссылкой на продукты
  const navigation = [
    { name: "Главная", href: "/" },
    { name: "Продукты", href: "/products" }, // Изменено с "#products" на "/products"
    { name: "Преимущества", href: "#features" },
    { name: "О нас", href: "#about" },
  ]

  return (
    <header className="bg-white shadow-sm border-b border-gray-200 sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo */}
          <Link href="/" className="flex items-center space-x-2 hover:opacity-80 transition-opacity">
            <div className="bg-blue-600 p-2 rounded-lg">
              <Shield className="h-6 w-6 text-white" />
            </div>
            <div>
              <span className="text-xl font-bold text-gray-900">СтрахПлатформа</span>
              <div className="text-xs text-gray-500">Надежная защита</div>
            </div>
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex space-x-8">
            {navigation.map((item) => (
              <Link
                key={item.name}
                href={item.href}
                className="text-gray-700 hover:text-blue-600 px-3 py-2 text-sm font-medium transition-colors duration-200 relative group"
              >
                {item.name}
                <span className="absolute bottom-0 left-0 w-0 h-0.5 bg-blue-600 transition-all duration-200 group-hover:w-full"></span>
              </Link>
            ))}
          </nav>

          {/* Desktop Actions */}
          <div className="hidden md:flex items-center space-x-4">
            <Link
              href="tel:+78001234567"
              className="flex items-center space-x-2 text-gray-700 hover:text-blue-600 transition-colors duration-200 px-3 py-2 rounded-lg hover:bg-blue-50"
            >
              <Phone className="h-4 w-4" />
              <div className="text-right">
                <div className="text-sm font-medium">8 (800) 123-45-67</div>
                <div className="text-xs text-gray-500">Бесплатно по России</div>
              </div>
            </Link>
            <div className="w-px h-8 bg-gray-300"></div>
            <Link
              href="http://localhost:8000/admin/"
              target="_blank"
              className="btn-primary flex items-center space-x-2 px-4 py-2"
            >
              <User className="h-4 w-4" />
              <span>Личный кабинет</span>
            </Link>
          </div>

          {/* Mobile menu button */}
          <button
            onClick={() => setIsMenuOpen(!isMenuOpen)}
            className="md:hidden p-2 rounded-lg text-gray-700 hover:text-blue-600 hover:bg-gray-100 transition-colors duration-200"
          >
            {isMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
          </button>
        </div>

        {/* Mobile Navigation */}
        {isMenuOpen && (
          <div className="md:hidden py-4 border-t border-gray-200 bg-white">
            <div className="space-y-2">
              {navigation.map((item) => (
                <Link
                  key={item.name}
                  href={item.href}
                  className="block px-3 py-3 text-gray-700 hover:text-blue-600 hover:bg-blue-50 rounded-lg transition-colors duration-200 font-medium"
                  onClick={() => setIsMenuOpen(false)}
                >
                  {item.name}
                </Link>
              ))}
              <div className="pt-4 border-t border-gray-200 space-y-3">
                <Link
                  href="tel:+78001234567"
                  className="flex items-center space-x-3 px-3 py-3 text-gray-700 hover:text-blue-600 hover:bg-blue-50 rounded-lg transition-colors duration-200"
                >
                  <Phone className="h-5 w-5" />
                  <div>
                    <div className="font-medium">8 (800) 123-45-67</div>
                    <div className="text-sm text-gray-500">Бесплатно по России</div>
                  </div>
                </Link>
                <Link
                  href="http://localhost:8000/admin/"
                  target="_blank"
                  className="w-full btn-primary flex items-center justify-center space-x-2 py-3"
                >
                  <User className="h-4 w-4" />
                  <span>Личный кабинет</span>
                </Link>
              </div>
            </div>
          </div>
        )}
      </div>
    </header>
  )
}

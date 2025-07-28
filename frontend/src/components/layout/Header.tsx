"use client"

import Link from "next/link"
import { useState } from "react"
import { Menu, X, Shield, Phone, User } from "lucide-react"

export function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  const navigation = [
    { name: "Главная", href: "/" },
    { name: "Продукты", href: "/#products" },
    { name: "Отследить заявку", href: "/track" },
    { name: "О нас", href: "/about" },
    { name: "Контакты", href: "/contacts" },
  ]

  return (
    <header className="bg-white shadow-sm border-b border-gray-200 sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo */}
          <Link href="/" className="flex items-center space-x-2">
            <div className="bg-blue-600 p-2 rounded-lg">
              <Shield className="h-6 w-6 text-white" />
            </div>
            <div>
              <span className="text-xl font-bold text-gray-900">СП</span>
              <span className="text-sm text-gray-600 ml-1">Страховая платформа</span>
            </div>
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex space-x-8">
            {navigation.map((item) => (
              <Link
                key={item.name}
                href={item.href}
                className="text-gray-700 hover:text-blue-600 px-3 py-2 text-sm font-medium transition-colors duration-200"
              >
                {item.name}
              </Link>
            ))}
          </nav>

          {/* Desktop Actions */}
          <div className="hidden md:flex items-center space-x-4">
            <Link
              href="tel:+78001234567"
              className="flex items-center space-x-1 text-gray-700 hover:text-blue-600 transition-colors duration-200"
            >
              <Phone className="h-4 w-4" />
              <span className="text-sm font-medium">8 (800) 123-45-67</span>
            </Link>
            <Link href="/admin" className="btn-primary flex items-center space-x-1">
              <User className="h-4 w-4" />
              <span>Админ панель</span>
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
          <div className="md:hidden py-4 border-t border-gray-200">
            <div className="space-y-2">
              {navigation.map((item) => (
                <Link
                  key={item.name}
                  href={item.href}
                  className="block px-3 py-2 text-gray-700 hover:text-blue-600 hover:bg-gray-50 rounded-lg transition-colors duration-200"
                  onClick={() => setIsMenuOpen(false)}
                >
                  {item.name}
                </Link>
              ))}
              <div className="pt-4 border-t border-gray-200 space-y-2">
                <Link
                  href="tel:+78001234567"
                  className="flex items-center space-x-2 px-3 py-2 text-gray-700 hover:text-blue-600 hover:bg-gray-50 rounded-lg transition-colors duration-200"
                >
                  <Phone className="h-4 w-4" />
                  <span>8 (800) 123-45-67</span>
                </Link>
                <Link
                  href="/admin"
                  className="flex items-center space-x-2 px-3 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors duration-200"
                >
                  <User className="h-4 w-4" />
                  <span>Админ панель</span>
                </Link>
              </div>
            </div>
          </div>
        )}
      </div>
    </header>
  )
}


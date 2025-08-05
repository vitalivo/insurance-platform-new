"use client"

import { useState } from "react"
import { useForm } from "react-hook-form"
import { zodResolver } from "@hookform/resolvers/zod"
import { z } from "zod"
import type { Product, CreateApplicationData } from "@/lib/api"
import { applicationsApi } from "@/lib/api"
import { LoadingSpinner } from "@/components/ui/LoadingSpinner"
import { CheckCircle, X, AlertCircle } from "lucide-react"

interface ApplicationFormProps {
  product: Product
  onSuccess?: (applicationNumber: string) => void
  onCancel?: () => void
}

// Базовая схема валидации
const baseSchema = z.object({
  full_name: z.string().min(2, "Имя должно содержать минимум 2 символа"),
  phone: z.string().min(10, "Введите корректный номер телефона"),
  email: z.string().email("Введите корректный email"),
})

export function ApplicationForm({ product, onSuccess, onCancel }: ApplicationFormProps) {
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [submitError, setSubmitError] = useState<string | null>(null)
  const [isSuccess, setIsSuccess] = useState(false)
  const [applicationNumber, setApplicationNumber] = useState<string>("")

  // Создаем динамическую схему валидации на основе полей продукта
  const createDynamicSchema = () => {
    const dynamicFields: Record<string, z.ZodTypeAny> = {}

    if (product.fields) {
      product.fields.forEach((field) => {
        let fieldSchema: z.ZodTypeAny

        switch (field.field_type) {
          case "email":
            fieldSchema = z.string().email("Введите корректный email")
            break
          case "phone":
            fieldSchema = z.string().min(10, "Введите корректный номер телефона")
            break
          case "number":
            fieldSchema = z.string().regex(/^\d+$/, "Введите только цифры")
            break
          case "date":
            fieldSchema = z.string().min(1, "Выберите дату")
            break
          default:
            fieldSchema = z.string().min(1, "Поле обязательно для заполнения")
        }

        if (!field.is_required) {
          fieldSchema = fieldSchema.optional().or(z.literal(""))
        }

        dynamicFields[field.name] = fieldSchema
      })
    }

    return baseSchema.extend(dynamicFields)
  }

  const schema = createDynamicSchema()
  type FormData = z.infer<typeof schema>

  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm<FormData>({
    resolver: zodResolver(schema),
  })

  const onSubmit = async (data: FormData) => {
    setIsSubmitting(true)
    setSubmitError(null)

    try {
      // Разделяем основные поля и дополнительные поля формы
      const { full_name, phone, email, ...formData } = data

      const applicationData: CreateApplicationData = {
        product: product.id,
        full_name,
        phone,
        email,
        form_data: formData,
      }

      const response = await applicationsApi.create(applicationData)
      setApplicationNumber(response.data.application_number)
      setIsSuccess(true)

      if (onSuccess) {
        onSuccess(response.data.application_number)
      }
    } catch (error: any) {
      setSubmitError(error.response?.data?.message || "Произошла ошибка при отправке заявки")
    } finally {
      setIsSubmitting(false)
    }
  }

  // Успешная отправка
  if (isSuccess) {
    return (
      <div className="text-center py-8">
        <CheckCircle className="h-16 w-16 text-green-500 mx-auto mb-4" />
        <h3 className="text-xl font-bold text-gray-900 mb-2">Заявка отправлена!</h3>
        <p className="text-gray-600 mb-4">
          Номер вашей заявки: <span className="font-bold text-blue-600">#{applicationNumber}</span>
        </p>
        <p className="text-sm text-gray-500 mb-6">Наш специалист свяжется с вами в ближайшее время</p>
        <button onClick={() => reset()} className="btn-secondary">
          Подать еще одну заявку
        </button>
      </div>
    )
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
      {/* Основные поля */}
      <div className="space-y-4">
        <div>
          <label htmlFor="full_name" className="block text-sm font-medium text-gray-700 mb-1">
            ФИО *
          </label>
          <input {...register("full_name")} type="text" className="input-field" placeholder="Введите ваше полное имя" />
          {errors.full_name && <p className="text-red-600 text-sm mt-1">{errors.full_name.message}</p>}
        </div>

        <div>
          <label htmlFor="phone" className="block text-sm font-medium text-gray-700 mb-1">
            Телефон *
          </label>
          <input {...register("phone")} type="tel" className="input-field" placeholder="+7 (999) 123-45-67" />
          {errors.phone && <p className="text-red-600 text-sm mt-1">{errors.phone.message}</p>}
        </div>

        <div>
          <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-1">
            Email *
          </label>
          <input {...register("email")} type="email" className="input-field" placeholder="your@email.com" />
          {errors.email && <p className="text-red-600 text-sm mt-1">{errors.email.message}</p>}
        </div>
      </div>

      {/* Динамические поля продукта */}
      {product.fields && product.fields.length > 0 && (
        <div className="border-t pt-6">
          <h4 className="text-lg font-medium text-gray-900 mb-4">Дополнительная информация</h4>
          <div className="space-y-4">
            {product.fields
              .sort((a, b) => a.sort_order - b.sort_order)
              .map((field) => (
                <div key={field.id}>
                  <label htmlFor={field.name} className="block text-sm font-medium text-gray-700 mb-1">
                    {field.label} {field.is_required && "*"}
                  </label>

                  {field.field_type === "select" ? (
                    <select {...register(field.name as keyof FormData)} className="input-field">
                      <option value="">Выберите вариант</option>
                      {field.options.map((option, index) => (
                        <option key={index} value={option}>
                          {option}
                        </option>
                      ))}
                    </select>
                  ) : field.field_type === "textarea" ? (
                    <textarea
                      {...register(field.name as keyof FormData)}
                      className="input-field"
                      rows={3}
                      placeholder={field.placeholder}
                    />
                  ) : field.field_type === "checkbox" ? (
                    <div className="flex items-center">
                      <input
                        {...register(field.name as keyof FormData)}
                        type="checkbox"
                        className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                      />
                      <label htmlFor={field.name} className="ml-2 text-sm text-gray-700">
                        {field.placeholder}
                      </label>
                    </div>
                  ) : (
                    <input
                      {...register(field.name as keyof FormData)}
                      type={field.field_type}
                      className="input-field"
                      placeholder={field.placeholder}
                    />
                  )}

                  {errors[field.name as keyof FormData] && (
                    <p className="text-red-600 text-sm mt-1">{errors[field.name as keyof FormData]?.message}</p>
                  )}
                </div>
              ))}
          </div>
        </div>
      )}

      {/* Ошибка отправки */}
      {submitError && (
        <div className="bg-red-50 border border-red-200 rounded-lg p-4 flex items-start space-x-3">
          <AlertCircle className="h-5 w-5 text-red-500 flex-shrink-0 mt-0.5" />
          <div>
            <h4 className="text-sm font-medium text-red-800">Ошибка отправки</h4>
            <p className="text-sm text-red-700 mt-1">{submitError}</p>
          </div>
        </div>
      )}

      {/* Кнопки */}
      <div className="flex space-x-4 pt-6">
        <button
          type="submit"
          disabled={isSubmitting}
          className="btn-primary flex-1 flex items-center justify-center space-x-2 py-3"
        >
          {isSubmitting ? (
            <>
              <LoadingSpinner size="sm" />
              <span>Отправка...</span>
            </>
          ) : (
            <span>Отправить заявку</span>
          )}
        </button>

        {onCancel && (
          <button type="button" onClick={onCancel} className="btn-secondary px-6 py-3">
            <X className="h-4 w-4" />
          </button>
        )}
      </div>

      {/* Согласие на обработку данных */}
      <p className="text-xs text-gray-500 text-center">
        Нажимая "Отправить заявку", вы соглашаетесь с{" "}
        <a href="/privacy" className="text-blue-600 hover:underline">
          политикой обработки персональных данных
        </a>
      </p>
    </form>
  )
}

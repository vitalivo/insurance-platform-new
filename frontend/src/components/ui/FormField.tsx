import type React from "react"
import { forwardRef } from "react"
import { cn } from "@/lib/utils"

interface FormFieldProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string
  error?: string
  required?: boolean
}

export const FormField = forwardRef<HTMLInputElement, FormFieldProps>(
  ({ label, error, required, className, ...props }, ref) => {
    return (
      <div className="space-y-1">
        {label && (
          <label className="block text-sm font-medium text-gray-700">
            {label} {required && <span className="text-red-500">*</span>}
          </label>
        )}
        <input
          ref={ref}
          className={cn("input-field", error && "border-red-300 focus:border-red-500 focus:ring-red-500", className)}
          {...props}
        />
        {error && <p className="text-red-600 text-sm">{error}</p>}
      </div>
    )
  },
)

FormField.displayName = "FormField"

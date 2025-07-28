from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Application, ApplicationStatus
from .views import export_applications

@admin.register(ApplicationStatus)
class ApplicationStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'is_final', 'sort_order', 'is_active']
    list_filter = ['is_final', 'is_active']
    ordering = ['sort_order']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = [
        'application_number', 'full_name', 'product', 
        'status', 'phone', 'created_at'
    ]
    list_filter = ['product', 'status', 'created_at']
    search_fields = ['application_number', 'full_name', 'phone', 'email']
    readonly_fields = ['application_number', 'created_at', 'updated_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('application_number', 'product', 'status')
        }),
        ('Данные клиента', {
            'fields': ('full_name', 'phone', 'email')
        }),
        ('Дополнительные данные', {
            'fields': ('form_data', 'admin_comment')
        }),
        ('Служебная информация', {
            'fields': ('created_at', 'updated_at', 'processed_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('export/', self.export_view, name='applications_export'),
        ]
        return custom_urls + urls
    
    def export_view(self, request):
        return export_applications(request)
    
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['export_url'] = 'export/'
        return super().changelist_view(request, extra_context)

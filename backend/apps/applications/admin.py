from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Application, ApplicationStatus

@admin.register(ApplicationStatus)
class ApplicationStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'color_display', 'is_final', 'sort_order']
    list_editable = ['sort_order']
    list_filter = ['is_final']
    ordering = ['sort_order']
    
    def color_display(self, obj):
        return format_html(
            '<div style="width: 20px; height: 20px; background-color: {}; border-radius: 3px; display: inline-block;"></div>',
            obj.color
        )
    color_display.short_description = 'Цвет'

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = [
        'application_number', 'full_name', 'product', 'status_display', 
        'created_at', 'notifications_status', 'admin_actions'
    ]
    list_filter = ['status', 'product', 'created_at', 'notifications_sent']
    search_fields = ['application_number', 'full_name', 'phone', 'email']
    readonly_fields = [
        'application_number', 'created_at', 'updated_at', 
        'notifications_sent', 'client_notified', 'admin_notified'
    ]
    ordering = ['-created_at']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('application_number', 'product', 'status', 'created_at')
        }),
        ('Данные клиента', {
            'fields': ('full_name', 'phone', 'email')
        }),
        ('Дополнительные данные', {
            'fields': ('form_data',),
            'classes': ('collapse',)
        }),
        ('Обработка', {
            'fields': ('admin_comment', 'processed_at')
        }),
        ('Уведомления', {
            'fields': ('notifications_sent', 'client_notified', 'admin_notified'),
            'classes': ('collapse',)
        }),
    )
    
    def status_display(self, obj):
        return format_html(
            '<span style="color: {}; font-weight: bold;">●</span> {}',
            obj.status.color,
            obj.status.name
        )
    status_display.short_description = 'Статус'
    
    def notifications_status(self, obj):
        icons = []
        if obj.client_notified:
            icons.append('<span style="color: green;" title="Клиент уведомлен">📧</span>')
        if obj.admin_notified:
            icons.append('<span style="color: blue;" title="Админ уведомлен">📱</span>')
        if obj.notifications_sent:
            icons.append('<span style="color: green;" title="Уведомления отправлены">✅</span>')
        
        return mark_safe(' '.join(icons)) if icons else '❌'
    notifications_status.short_description = 'Уведомления'
    
    def admin_actions(self, obj):
        return format_html(
            '<a href="{}">Повторить уведомления</a>',
            reverse('admin:resend_notifications', args=[obj.pk])
        )
    admin_actions.short_description = 'Действия'
    
    def save_model(self, request, obj, form, change):
        """Переопределяем сохранение для отслеживания изменений статуса"""
        if change:
            # Получаем старый объект для сравнения
            old_obj = Application.objects.get(pk=obj.pk)
            old_status = old_obj.status
            
            # Сохраняем объект
            super().save_model(request, obj, form, change)
            
            # Если статус изменился, отправляем уведомление
            if old_status != obj.status:
                from .tasks import send_status_change_notification
                send_status_change_notification.delay(obj.id, old_status.name, obj.status.name)
        else:
            super().save_model(request, obj, form, change)

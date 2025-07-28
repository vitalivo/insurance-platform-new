from django.contrib import admin
from .models import NotificationTemplate, NotificationLog

@admin.register(NotificationTemplate)
class NotificationTemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'template_type', 'is_active']
    list_filter = ['template_type', 'is_active']
    search_fields = ['name', 'subject']

@admin.register(NotificationLog)
class NotificationLogAdmin(admin.ModelAdmin):
    list_display = ['notification_type', 'recipient', 'status', 'created_at']
    list_filter = ['notification_type', 'status', 'created_at']
    search_fields = ['recipient', 'subject']
    readonly_fields = ['created_at', 'sent_at']
    ordering = ['-created_at']

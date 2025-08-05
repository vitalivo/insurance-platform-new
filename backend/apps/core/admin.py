from django.contrib import admin
from .models import PageContent, SiteSettings

@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'section_name', 'content_key', 'content_type', 'content_value_preview']
    list_filter = ['page_name', 'section_name', 'content_type']
    search_fields = ['content_key', 'content_value']
    ordering = ['page_name', 'section_name', 'content_key']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('page_name', 'section_name', 'content_key', 'content_type')
        }),
        ('Контент', {
            'fields': ('content_value',)
        }),
    )
    
    def content_value_preview(self, obj):
        """Превью значения контента"""
        if len(obj.content_value) > 50:
            return obj.content_value[:50] + '...'
        return obj.content_value
    content_value_preview.short_description = 'Превью контента'
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Добавляем help_text для полей
        form.base_fields['page_name'].help_text = 'Название страницы (например: products, home)'
        form.base_fields['section_name'].help_text = 'Название секции (например: hero, products_list)'
        form.base_fields['content_key'].help_text = 'Ключ контента (например: title, description)'
        return form

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Отображение продуктов', {
            'fields': (
                'products_per_row_desktop',
                'products_per_row_tablet', 
                'products_per_row_mobile'
            )
        }),
        ('Сортировка и фильтрация', {
            'fields': ('products_sort_by', 'show_featured_first')
        }),
    )
    
    def has_add_permission(self, request):
        # Разрешить создание только если нет записей
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Запретить удаление настроек
        return False
    
    def changelist_view(self, request, extra_context=None):
        # Если нет настроек, создать по умолчанию
        if not SiteSettings.objects.exists():
            SiteSettings.objects.create()
        return super().changelist_view(request, extra_context)

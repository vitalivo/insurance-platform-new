from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import AdminProfile

class AdminProfileInline(admin.StackedInline):
    model = AdminProfile
    can_delete = False
    verbose_name_plural = 'Профиль'

class UserAdmin(BaseUserAdmin):
    inlines = (AdminProfileInline,)

# Перерегистрируем User модель
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(AdminProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'telegram_username', 'position']
    search_fields = ['user__username', 'user__email', 'phone']

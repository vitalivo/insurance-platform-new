from django.db import models
from django.contrib.auth.models import User
from apps.core.models import BaseModel

class AdminProfile(BaseModel):
    """Профиль администратора"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    phone = models.CharField('Телефон', max_length=20, blank=True)
    telegram_username = models.CharField('Telegram', max_length=100, blank=True)
    position = models.CharField('Должность', max_length=100, blank=True)
    avatar = models.ImageField('Аватар', upload_to='avatars/', blank=True)
    
    class Meta:
        verbose_name = 'Профиль администратора'
        verbose_name_plural = 'Профили администраторов'
    
    def __str__(self):
        return f"Профиль {self.user.get_full_name() or self.user.username}"

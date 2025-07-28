from django.db import models
from django.utils import timezone

class TimeStampedModel(models.Model):
    """Абстрактная модель с временными метками"""
    created_at = models.DateTimeField('Дата создания', default=timezone.now)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        abstract = True

class ActiveManager(models.Manager):
    """Менеджер для активных записей"""
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class BaseModel(TimeStampedModel):
    """Базовая модель с общими полями"""
    is_active = models.BooleanField('Активно', default=True)
    
    objects = models.Manager()
    active = ActiveManager()

    class Meta:
        abstract = True

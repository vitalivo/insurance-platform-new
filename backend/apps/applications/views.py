from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from openpyxl import Workbook
from .models import Application, ApplicationStatus
from .serializers import (
    ApplicationCreateSerializer, 
    ApplicationDetailSerializer,
    ApplicationStatusSerializer,
    ApplicationListSerializer
)

class ApplicationCreateView(generics.CreateAPIView):
    """Создание новой заявки"""
    serializer_class = ApplicationCreateSerializer
    
    def perform_create(self, serializer):
        # Устанавливаем начальный статус
        initial_status = ApplicationStatus.active.first()
        application = serializer.save(status=initial_status)
        
        # Отправляем уведомления
        from apps.notifications.tasks import send_application_notifications
        send_application_notifications.delay(application.id)

class ApplicationDetailView(generics.RetrieveAPIView):
    """Детали заявки по номеру"""
    serializer_class = ApplicationDetailSerializer
    lookup_field = 'application_number'
    
    def get_object(self):
        app_number = self.kwargs.get('application_number')
        return get_object_or_404(
            Application.objects.select_related('product', 'status'),
            application_number=app_number
        )

class ApplicationStatusListView(generics.ListAPIView):
    """Список статусов заявок"""
    queryset = ApplicationStatus.active.all()
    serializer_class = ApplicationStatusSerializer

@api_view(['GET'])
def export_applications(request):
    """Экспорт заявок в Excel"""
    applications = Application.objects.select_related('product', 'status').all()
    
    # Создаем Excel файл
    wb = Workbook()
    ws = wb.active
    ws.title = "Заявки"
    
    # Заголовки
    headers = [
        'Номер заявки', 'Дата создания', 'Продукт', 'ФИО',
        'Телефон', 'Email', 'Статус', 'Комментарий'
    ]
    ws.append(headers)
    
    # Данные
    for app in applications:
        ws.append([
            app.application_number,
            app.created_at.strftime('%d.%m.%Y %H:%M'),
            app.product.name,
            app.full_name,
            app.phone,
            app.email,
            app.status.name,
            app.admin_comment or ''
        ])
    
    # Настройка ответа
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=applications.xlsx'
    wb.save(response)
    
    return response

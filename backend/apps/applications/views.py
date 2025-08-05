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
import logging
import json

logger = logging.getLogger(__name__)

class ApplicationListCreateView(generics.ListCreateAPIView):
    """Список заявок (GET) и создание новой заявки (POST)"""
    queryset = Application.objects.select_related('product', 'status').all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ApplicationCreateSerializer
        return ApplicationListSerializer
    
    def create(self, request, *args, **kwargs):
        """Переопределяем create для добавления логирования"""
        logger.debug(f"=== СОЗДАНИЕ ЗАЯВКИ ===")
        logger.debug(f"Headers: {dict(request.headers)}")
        logger.debug(f"Content-Type: {request.content_type}")
        logger.debug(f"Data: {request.data}")
        # Убираем request.body - он уже прочитан DRF
        
        try:
            # Проверяем, есть ли продукт
            product_id = request.data.get('product')
            if product_id:
                from apps.products.models import Product
                try:
                    product = Product.objects.get(id=product_id)
                    logger.debug(f"Найден продукт: {product.name}")
                except Product.DoesNotExist:
                    logger.error(f"Продукт с ID {product_id} не найден")
                    return Response(
                        {'error': f'Продукт с ID {product_id} не найден'}, 
                        status=status.HTTP_400_BAD_REQUEST
                    )
            
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                logger.debug("Данные валидны, создаем заявку...")
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                logger.info(f"Заявка успешно создана: {serializer.data}")
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                logger.error(f"Ошибки валидации: {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
        except Exception as e:
            logger.error(f"Неожиданная ошибка при создании заявки: {str(e)}")
            import traceback
            logger.error(f"Traceback: {traceback.format_exc()}")
            return Response(
                {'error': 'Внутренняя ошибка сервера'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def perform_create(self, serializer):
        # Устанавливаем начальный статус
        initial_status = ApplicationStatus.objects.first()
        if not initial_status:
            # Создаем статус по умолчанию, если его нет
            initial_status = ApplicationStatus.objects.create(
                name='Новая',
                color='#3B82F6',
                description='Новая заявка, ожидает обработки'
            )
            logger.info(f"Создан статус по умолчанию: {initial_status.name}")
        
        application = serializer.save(status=initial_status)
        logger.info(f"Создана заявка: {application.application_number}")

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
    queryset = ApplicationStatus.objects.all()
    serializer_class = ApplicationStatusSerializer

@api_view(['GET'])
def test_api(request):
    """Тестовый endpoint"""
    return Response({
        'message': 'API работает!',
        'applications_count': Application.objects.count(),
        'statuses_count': ApplicationStatus.objects.count()
    })

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

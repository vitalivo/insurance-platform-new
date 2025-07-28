from django.core.management.base import BaseCommand
from django.db import transaction
from apps.products.models import Product, ProductField
from apps.applications.models import ApplicationStatus
from apps.notifications.models import NotificationTemplate

class Command(BaseCommand):
    help = 'Загрузка начальных данных'

    def handle(self, *args, **options):
        self.stdout.write('Загрузка начальных данных...')
        
        try:
            with transaction.atomic():
                # Создаем статусы заявок
                statuses = [
                    {'name': 'Новая', 'color': '#3B82F6', 'description': 'Заявка только что поступила'},
                    {'name': 'В обработке', 'color': '#F59E0B', 'description': 'Заявка рассматривается'},
                    {'name': 'Требует уточнения', 'color': '#EF4444', 'description': 'Нужны дополнительные данные'},
                    {'name': 'Одобрена', 'color': '#10B981', 'description': 'Заявка одобрена', 'is_final': True},
                    {'name': 'Отклонена', 'color': '#6B7280', 'description': 'Заявка отклонена', 'is_final': True},
                ]
                
                for i, status_data in enumerate(statuses):
                    status, created = ApplicationStatus.objects.get_or_create(
                        name=status_data['name'],
                        defaults={
                            'color': status_data['color'],
                            'description': status_data['description'],
                            'is_final': status_data.get('is_final', False),
                            'sort_order': i  # Используем sort_order, не order
                        }
                    )
                    if created:
                        self.stdout.write(f'Создан статус: {status.name}')
                
                # Создаем продукты
                products_data = [
                    {
                        'name': 'ОСАГО',
                        'slug': 'osago',
                        'product_type': 'osago',
                        'description': 'Обязательное страхование автогражданской ответственности владельцев транспортных средств',
                        'short_description': 'Обязательное страхование автогражданской ответственности',
                        'icon': 'car',
                        'fields': [
                            {'name': 'vehicle_brand', 'field_type': 'text', 'label': 'Марка автомобиля', 'is_required': True},
                            {'name': 'vehicle_model', 'field_type': 'text', 'label': 'Модель автомобиля', 'is_required': True},
                            {'name': 'vehicle_year', 'field_type': 'number', 'label': 'Год выпуска', 'is_required': True},
                            {'name': 'license_plate', 'field_type': 'text', 'label': 'Государственный номер', 'is_required': True},
                        ]
                    },
                    {
                        'name': 'КАСКО',
                        'slug': 'kasko',
                        'product_type': 'kasko',
                        'description': 'Добровольное страхование автотранспорта от угона и ущерба',
                        'short_description': 'Добровольное страхование автотранспорта от угона и ущерба',
                        'icon': 'shield',
                        'fields': [
                            {'name': 'vehicle_brand', 'field_type': 'text', 'label': 'Марка автомобиля', 'is_required': True},
                            {'name': 'vehicle_model', 'field_type': 'text', 'label': 'Модель автомобиля', 'is_required': True},
                            {'name': 'vehicle_year', 'field_type': 'number', 'label': 'Год выпуска', 'is_required': True},
                            {'name': 'vehicle_cost', 'field_type': 'number', 'label': 'Стоимость автомобиля', 'is_required': True},
                            {'name': 'parking_type', 'field_type': 'select', 'label': 'Тип парковки', 'is_required': True,
                             'options': ['Гараж', 'Охраняемая стоянка', 'Двор', 'Улица']},
                        ]
                    },
                    {
                        'name': 'Недвижимость',
                        'slug': 'property',
                        'product_type': 'property',
                        'description': 'Страхование квартир, домов и личного имущества',
                        'short_description': 'Страхование квартир, домов и личного имущества',
                        'icon': 'home',
                        'fields': [
                            {'name': 'property_type', 'field_type': 'select', 'label': 'Тип недвижимости', 'is_required': True,
                             'options': ['Квартира', 'Дом', 'Дача', 'Коммерческая недвижимость']},
                            {'name': 'property_address', 'field_type': 'textarea', 'label': 'Адрес объекта', 'is_required': True},
                            {'name': 'property_area', 'field_type': 'number', 'label': 'Площадь (кв.м)', 'is_required': True},
                            {'name': 'property_cost', 'field_type': 'number', 'label': 'Стоимость имущества', 'is_required': True},
                        ]
                    },
                    {
                        'name': 'Несчастный случай',
                        'slug': 'accident',
                        'product_type': 'accident',
                        'description': 'Страхование от несчастных случаев и болезней',
                        'short_description': 'Страхование от несчастных случаев и болезней',
                        'icon': 'heart-pulse',
                        'fields': [
                            {'name': 'insured_name', 'field_type': 'text', 'label': 'ФИО застрахованного', 'is_required': True},
                            {'name': 'birth_date', 'field_type': 'date', 'label': 'Дата рождения', 'is_required': True},
                            {'name': 'profession', 'field_type': 'text', 'label': 'Профессия', 'is_required': True},
                            {'name': 'coverage_amount', 'field_type': 'number', 'label': 'Страховая сумма', 'is_required': True},
                        ]
                    },
                    {
                        'name': 'Ипотека',
                        'slug': 'mortgage',
                        'product_type': 'mortgage',
                        'description': 'Страхование жизни и здоровья заемщика по ипотеке',
                        'short_description': 'Страхование жизни и здоровья заемщика по ипотеке',
                        'icon': 'building',
                        'fields': [
                            {'name': 'loan_amount', 'field_type': 'number', 'label': 'Сумма кредита', 'is_required': True},
                            {'name': 'loan_term', 'field_type': 'number', 'label': 'Срок кредита (лет)', 'is_required': True},
                            {'name': 'bank_name', 'field_type': 'text', 'label': 'Название банка', 'is_required': True},
                            {'name': 'property_address', 'field_type': 'textarea', 'label': 'Адрес недвижимости', 'is_required': True},
                        ]
                    },
                    {
                        'name': 'Клещ',
                        'slug': 'tick',
                        'product_type': 'tick',
                        'description': 'Страхование от укуса клеща',
                        'short_description': 'Страхование от укуса клеща',
                        'icon': 'bug',
                        'fields': [
                            {'name': 'insured_name', 'field_type': 'text', 'label': 'ФИО застрахованного', 'is_required': True},
                            {'name': 'birth_date', 'field_type': 'date', 'label': 'Дата рождения', 'is_required': True},
                            {'name': 'region', 'field_type': 'select', 'label': 'Регион проживания', 'is_required': True,
                             'options': ['Москва и МО', 'Санкт-Петербург и ЛО', 'Другие регионы']},
                            {'name': 'coverage_period', 'field_type': 'select', 'label': 'Период страхования', 'is_required': True,
                             'options': ['3 месяца', '6 месяцев', '12 месяцев']},
                        ]
                    },
                ]
                
                for i, product_data in enumerate(products_data):
                    fields_data = product_data.pop('fields')
                    product, created = Product.objects.get_or_create(
                        slug=product_data['slug'],
                        defaults={**product_data, 'sort_order': i}
                    )
                    
                    if created:
                        self.stdout.write(f'Создан продукт: {product.name}')
                        
                        # Создаем поля для продукта
                        for j, field_data in enumerate(fields_data):
                            ProductField.objects.create(
                                product=product,
                                sort_order=j,
                                **field_data
                            )
                
                # Создаем шаблоны уведомлений
                templates = [
                    {
                        'name': 'new_application_client',
                        'template_type': 'email_client',
                        'subject': 'Ваша заявка №{{ application_number }} принята',
                        'content': '''
                        <h2>Спасибо за обращение!</h2>
                        <p>Ваша заявка на страхование "{{ product_name }}" принята к рассмотрению.</p>
                        <p><strong>Номер заявки:</strong> {{ application_number }}</p>
                        <p><strong>Дата подачи:</strong> {{ created_at }}</p>
                        <p>Мы свяжемся с вами в ближайшее время для уточнения деталей.</p>
                        <p>С уважением,<br>Команда страховой компании</p>
                        '''
                    },
                ]
                
                for template_data in templates:
                    template, created = NotificationTemplate.objects.get_or_create(
                        name=template_data['name'],
                        defaults=template_data
                    )
                    if created:
                        self.stdout.write(f'Создан шаблон: {template.name}')
                
                self.stdout.write(self.style.SUCCESS('Начальные данные загружены успешно!'))
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при загрузке данных: {e}'))
            raise

from rest_framework import serializers
from .models import Application, ApplicationStatus
from apps.products.serializers import ProductListSerializer

class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationStatus
        fields = ['id', 'name', 'color', 'description']

class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['product', 'full_name', 'phone', 'email', 'form_data']
    
    def validate_phone(self, value):
        from apps.core.utils import validate_phone, format_phone
        if not validate_phone(value):
            raise serializers.ValidationError("Некорректный номер телефона")
        return format_phone(value)
    
    def validate_email(self, value):
        from apps.core.utils import validate_email
        if not validate_email(value):
            raise serializers.ValidationError("Некорректный email адрес")
        return value.lower()

class ApplicationDetailSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    status = ApplicationStatusSerializer(read_only=True)
    
    class Meta:
        model = Application
        fields = [
            'id', 'application_number', 'product', 'status',
            'full_name', 'phone', 'email', 'form_data',
            'admin_comment', 'created_at', 'processed_at'
        ]

class ApplicationListSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    status_name = serializers.CharField(source='status.name', read_only=True)
    status_color = serializers.CharField(source='status.color', read_only=True)
    
    class Meta:
        model = Application
        fields = [
            'id', 'application_number', 'product_name', 'status_name',
            'status_color', 'full_name', 'phone', 'email', 'created_at'
        ]

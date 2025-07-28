from rest_framework import serializers
from django.contrib.auth.models import User
from .models import AdminProfile

class AdminProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    
    class Meta:
        model = AdminProfile
        fields = [
            'username', 'email', 'first_name', 'last_name',
            'phone', 'telegram_username', 'position', 'avatar'
        ]
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        
        # Обновляем данные пользователя
        for attr, value in user_data.items():
            setattr(instance.user, attr, value)
        instance.user.save()
        
        # Обновляем профиль
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance

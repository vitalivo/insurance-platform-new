from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import AdminProfile
from .serializers import AdminProfileSerializer

class AdminProfileView(generics.RetrieveUpdateAPIView):
    """Просмотр и редактирование профиля администратора"""
    serializer_class = AdminProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        profile, created = AdminProfile.objects.get_or_create(user=self.request.user)
        return profile

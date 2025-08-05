from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PageContent, SiteSettings
from .serializers import PageContentSerializer, SiteSettingsSerializer

class PageContentListView(generics.ListAPIView):
    """Получение контента страниц"""
    queryset = PageContent.objects.all()
    serializer_class = PageContentSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        page_name = self.request.query_params.get('page', None)
        if page_name:
            queryset = queryset.filter(page_name=page_name)
        return queryset

@api_view(['GET'])
def site_settings_view(request):
    """Получение настроек сайта"""
    settings, created = SiteSettings.objects.get_or_create()
    serializer = SiteSettingsSerializer(settings)
    return Response(serializer.data)

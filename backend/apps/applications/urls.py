from django.urls import path
from .views import (
    ApplicationListCreateView,
    ApplicationDetailView,
    ApplicationStatusListView,
    export_applications,
    test_api
)

app_name = 'applications'

urlpatterns = [
    # Тестовый endpoint
    path('test/', test_api, name='test-api'),
    
    # Основные endpoints
    path('applications/', ApplicationListCreateView.as_view(), name='application-list-create'),
    path('applications/<str:application_number>/', ApplicationDetailView.as_view(), name='application-detail'),
    path('statuses/', ApplicationStatusListView.as_view(), name='status-list'),
    path('export/applications/', export_applications, name='export-applications'),
]

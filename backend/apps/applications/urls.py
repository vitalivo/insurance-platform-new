from django.urls import path
from .views import (
    ApplicationCreateView,
    ApplicationDetailView, 
    ApplicationStatusListView,
    export_applications
)

app_name = 'applications'

urlpatterns = [
    path('applications/', ApplicationCreateView.as_view(), name='application-create'),
    path('applications/<str:application_number>/', ApplicationDetailView.as_view(), name='application-detail'),
    path('statuses/', ApplicationStatusListView.as_view(), name='status-list'),
    path('export/applications/', export_applications, name='export-applications'),
]

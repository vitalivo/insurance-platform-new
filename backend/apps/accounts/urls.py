from django.urls import path
from .views import AdminProfileView

app_name = 'accounts'

urlpatterns = [
    path('profile/', AdminProfileView.as_view(), name='admin-profile'),
]


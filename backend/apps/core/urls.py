from django.urls import path
from .views import PageContentListView, site_settings_view

app_name = 'core'

urlpatterns = [
    path('page-content/', PageContentListView.as_view(), name='page-content'),
    path('site-settings/', site_settings_view, name='site-settings'),
]

from django.urls import path
from .views import (
    CompanyListCreateView,
    CompanyDetailView,
    EmployeeListCreateView,
    EmployeeDetailView,
    CompanyManagerListCreateView,
    CompanyManagerDetailView,
    DeviceListCreateView,
    DeviceDetailView,
    DeviceLogInfoListCreateView,
    DeviceLogDetailView,

)

urlpatterns = [
    path('companies/', CompanyListCreateView.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('company-managers/', CompanyManagerListCreateView.as_view(), name='company-manager-list'),
    path('company-managers/<int:pk>/', CompanyManagerDetailView.as_view(), name='company-manager-detail'),
    path('devices/', DeviceListCreateView.as_view(), name='device-list'),
    path('devices/<int:pk>/', DeviceDetailView.as_view(), name='device-detail'),
    path('device-logs/', DeviceLogInfoListCreateView.as_view(), name='device-log-list'),
    path('device-logs/<int:pk>/', DeviceLogDetailView.as_view(), name='device-log-detail'),
]
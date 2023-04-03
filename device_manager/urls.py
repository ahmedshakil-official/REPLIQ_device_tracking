from django.urls import path
from .views import (
    CompanyListCreateView,
    CompanyDetailView,
    EmployeeListCreateView,
    EmployeeDetailView,

)

urlpatterns = [
    path('companies/', CompanyListCreateView.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),

]
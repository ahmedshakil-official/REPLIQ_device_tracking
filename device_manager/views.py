from rest_framework import generics
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Company, Employee, CompanyManager, Device, DeviceLogInfo
from .serializers import (CompanySerializer,
                          EmployeeSerializer,
                          CompanyManagerSerializer,
                          DeviceSerializer,
                          DeviceLogInfoSerializer)


class CompanyListCreateView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        return Company.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_object(self):
        return get_object_or_404(Company, pk=self.kwargs['pk'])


class EmployeeListCreateView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_object(self):
        return get_object_or_404(Employee, pk=self.kwargs['pk'])


class CompanyManagerListCreateView(generics.ListCreateAPIView):
    serializer_class = CompanyManagerSerializer

    def get_queryset(self):
        return CompanyManager.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CompanyManagerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanyManagerSerializer

    def get_object(self):
        return get_object_or_404(CompanyManager, pk=self.kwargs['pk'])


class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.request.method == 'POST':
            context['company_id'] = self.request.data.get('company_id')
        return context

    def perform_create(self, serializer):
        company_id = self.request.data.get('company_id')
        company = get_object_or_404(Company, id=company_id)
        serializer.save(company=company, checked_out=False, checked_out_to=None, condition='good')


class DeviceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeviceSerializer

    def get_object(self):
        return get_object_or_404(Device, pk=self.kwargs['pk'])


class DeviceLogInfoListCreateView(generics.ListCreateAPIView):
    serializer_class = DeviceLogInfoSerializer

    def get_queryset(self):
        return DeviceLogInfo.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DeviceLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeviceLogInfoSerializer

    def get_object(self):
        return get_object_or_404(DeviceLogInfo, pk=self.kwargs['pk'])

from rest_framework import generics
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Company, Employee
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

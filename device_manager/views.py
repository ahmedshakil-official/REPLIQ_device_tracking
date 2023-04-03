from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Company
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

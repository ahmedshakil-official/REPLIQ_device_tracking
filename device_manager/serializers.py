from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Company, Employee, CompanyManager, Device, DeviceLogInfo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CompanySerializer(serializers.ModelSerializer):
    employees = UserSerializer(many=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'address', 'authority', 'authority_email', 'authority_phone', 'employees']



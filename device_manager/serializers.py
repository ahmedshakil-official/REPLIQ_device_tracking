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


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'user']


class CompanyManagerSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    company = CompanySerializer()

    class Meta:
        model = CompanyManager
        fields = ['id', 'employee', 'company']


class DeviceSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    assigned_to = EmployeeSerializer()

    class Meta:
        model = Device
        fields = ['id', 'name', 'model', 'serial_number', 'category', 'company', 'assigned_to', 'assigned_time']


class DeviceLogInfoSerializer(serializers.ModelSerializer):
    device = DeviceSerializer()
    checked_out_to = EmployeeSerializer()
    checked_in_by = EmployeeSerializer()

    class Meta:
        model = DeviceLogInfo
        fields = ['id', 'device', 'checked_out_to', 'checked_out_from', 'checked_in_by', 'checked_in_at', 'condition']
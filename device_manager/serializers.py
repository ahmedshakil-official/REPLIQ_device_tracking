from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Company, Employee, CompanyManager, Device, DeviceLogInfo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class EmployeeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source='username')

    class Meta:
        model = Employee
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'location', 'employees']

    def create(self, validated_data):
        employees_data = validated_data.pop('employees')
        company = Company.objects.create(**validated_data)
        for employee_data in employees_data:
            Employee.objects.create(company=company, **employee_data)
        return company


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

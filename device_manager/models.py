from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200, default='')
    company = models.ForeignKey('Company', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=255)

    authority = models.CharField(max_length=255)
    authority_email = models.EmailField()
    authority_phone = models.CharField(max_length=15)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Device(models.Model):
    CATEGORY_PHONE = 'Phone'
    CATEGORY_TABLET = 'Tablet'
    CATEGORY_LAPTOP = 'Laptop'
    CATEGORY_OTHER = 'Other'

    CATEGORY_CHOICES = [
        ('P', CATEGORY_PHONE),
        ('T', CATEGORY_TABLET),
        ('L', CATEGORY_LAPTOP),
        ('O', CATEGORY_OTHER),
    ]

    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default=CATEGORY_OTHER)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)
    assigned_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class DeviceLogInfo(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checked_out_to = models.ForeignKey(Employee, related_name='checked_out_to', on_delete=models.CASCADE)
    checked_out_from = models.DateTimeField(auto_now_add=True)
    checked_in_by = models.ForeignKey(Employee, related_name='checked_in_by', on_delete=models.CASCADE)
    checked_in_at = models.DateTimeField(null=True, blank=True)
    condition = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.device.name} - {self.checked_out_to.user.username}'

    class Meta:
        ordering = ['checked_out_from', 'checked_in_at']

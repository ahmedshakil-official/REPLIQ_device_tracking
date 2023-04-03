from django.db import models
from django.contrib.auth.models import User


# Model for specific company
class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    authority = models.CharField(max_length=255)
    authority_email = models.EmailField()
    authority_phone = models.CharField(max_length=15)
    # defining employees who will work for this company
    employees = models.ManyToManyField(User, related_name='companies', through='CompanyManager')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


# create user model for the employee
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_managers = models.ManyToManyField('CompanyManager', related_name='employees')

    def __str__(self):
        return self.user.username


# Create a model for manging multiple company and employees
class CompanyManager(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.employee} - {self.company}'


# Device model for storing device information
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
    # Name of the company providing this device
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # Employee who is getting this device
    assigned_to = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)
    assigned_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


# Model for tracking device log
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

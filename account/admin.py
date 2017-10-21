from django.contrib import admin
from .models import Employee
from .models import Administrator
from .models import Donor

class EmployeeList(admin.ModelAdmin):
    list_display = ('emp_number', 'name', 'city', 'cell_phone')
    list_filter = ('emp_number', 'name', 'city')
    search_fields = ('emp_number', 'name')
    ordering = ['emp_number']

class AdministratorList(admin.ModelAdmin):
    list_display = ('emp_number', 'name', 'city', 'cell_phone')
    list_filter = ('emp_number', 'name', 'city')
    search_fields = ('emp_number', 'name')
    ordering = ['emp_number']

class DonorList(admin.ModelAdmin):
    list_display = ('emp_number', 'name', 'city', 'cell_phone')
    list_filter = ('emp_number', 'name', 'city')
    search_fields = ('emp_number', 'name')
    ordering = ['emp_number']

admin.site.register(Employee, EmployeeList)
admin.site.register(Administrator, AdministratorList)
admin.site.register(Donor, DonorList)

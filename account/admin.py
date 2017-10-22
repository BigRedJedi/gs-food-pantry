from django.contrib import admin
from .models import Employee
from .models import Administrator
from .models import Donor
from .models import Client
from .models import Item

class EmployeeList(admin.ModelAdmin):
    list_display = ('emp_number', 'first_name', 'last_name', 'city', 'cell_phone')
    list_filter = ('emp_number', 'first_name', 'last_name', 'city')
    search_fields = ('emp_number', 'first_name', 'last_name',)
    ordering = ['emp_number']

class AdministratorList(admin.ModelAdmin):
    list_display = ('emp_number', 'first_name', 'last_name', 'city', 'cell_phone')
    list_filter = ('emp_number', 'first_name', 'last_name', 'city')
    search_fields = ('emp_number', 'first_name', 'last_name',)
    ordering = ['emp_number']

class DonorList(admin.ModelAdmin):
    list_display = ('donor_number', 'first_name', 'last_name', 'city', 'cell_phone')
    list_filter = ('donor_number', 'first_name', 'last_name', 'city')
    search_fields = ('donor_number', 'first_name', 'last_name',)
    ordering = ['donor_number']

class ClientList(admin.ModelAdmin):
    list_display = ('client_number', 'first_name', 'last_name', 'city', 'cell_phone')
    list_filter = ('client_number', 'first_name', 'last_name', 'city')
    search_fields = ('client_number', 'first_name', 'last_name',)
    ordering = ['client_number']

class ItemList(admin.ModelAdmin):
    list_display = ('item_number', 'item_name')
    list_filter = ('item_number', 'item_name')
    search_fields = ('item_number', 'item_name')
    ordering = ['item_number']

admin.site.register(Employee, EmployeeList)
admin.site.register(Administrator, AdministratorList)
admin.site.register(Donor, DonorList)
admin.site.register(Client, ClientList)
admin.site.register(Item, ItemList)


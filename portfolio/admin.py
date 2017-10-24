from django.contrib import admin
from .models import Client, Item, Employee, Donor, Visit

class ClientList(admin.ModelAdmin):
    list_display = ('client_number', 'name', 'city', 'cell_phone')
    list_filter = ('client_number', 'name', 'city')
    search_fields = ('client_number', 'name')
    ordering = ['client_number']

class ItemList(admin.ModelAdmin):
    list_display = ('item_number', 'item_type', 'description', 'qty_on_hand')
    list_filter = ('item_number', 'item_type')
    search_fields = ('item_number', 'item_type')
    ordering = ['item_number']

class EmployeeList(admin.ModelAdmin):
    list_display = ('emp_number','name', 'address', 'city', 'state')
    list_filter = ('emp_number','name', 'address')
    search_fields = ('emp_number', 'name')
    ordering = ['emp_number']

class DonorList(admin.ModelAdmin):
    list_display = ('donor_number','name', 'address', 'city', 'state')
    list_filter = ('donor_number','name', 'address')
    search_fields = ('donor_number','name')
    ordering = ['donor_number']


class VisitList(admin.ModelAdmin):
    list_display = ('visit_number', 'visit_type')
    list_filter = ('visit_number', 'visit_type')
    search_fields = ('visit_number', 'visit_type')
    ordering = ['visit_number']

admin.site.register(Employee, EmployeeList)
admin.site.register(Visit, VisitList)
admin.site.register(Donor, DonorList)
admin.site.register(Client, ClientList)
admin.site.register(Item, ItemList)


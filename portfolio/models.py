from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    client_number = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField(blank=False, null=False)
    email = models.EmailField(max_length=200)
    cell_phone = models.IntegerField(blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.client_number)


class Item(models.Model):
    name = models.CharField(max_length=50)
    item_number = models.IntegerField(blank=False, null=False)
    item_type = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    qty_on_hand = models.IntegerField(blank=False, null=False)
    expired_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.item_number)


class Employee(models.Model):
    emp_number = models.IntegerField(blank=False, null=False)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField(blank=False, null=False)
    email = models.EmailField(max_length=200)
    cell_phone = models.IntegerField(blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)


    def created(self):
        self.recent_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.emp_number)


class Donor(models.Model):
    donor_number = models.IntegerField(blank=False, null=False)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    cell_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.recent_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.donor_number)


class Visit(models.Model):
    client = models.ForeignKey(Client, default=1, related_name='visits')
    employee = models.ForeignKey(Employee, default=1, related_name='visits')
    visit_number = models.IntegerField(primary_key=True, blank=False, null=False, default=0)
    visit_type = models.CharField(max_length=50)
    visit_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50,default='')
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.visit_number)

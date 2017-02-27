import uuid
from django.db import models


""" DOCK & SHIP MODELS """


class Dock(models.Model):
    dock_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    docked_ship = models.OneToOneField('Ship', related_name='dock', null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


class DockManifest(models.Model):
    dock = models.ForeignKey(Dock, related_name='manifests')
    ship = models.ForeignKey('Ship')
    arrival = models.DateTimeField()
    departure = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


class Ship(models.Model):
    ship_id = models.CharField(unique=True, max_length=50, db_index=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    captain = models.ForeignKey('ShipCaptain', null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


class Container(models.Model):
    container_id = models.IntegerField(unique=True, max_length=50, db_index=True)
    hazards = models.ManyToManyField('ContentHazard')
    ship = models.ForeignKey('Ship', related_name='containers', on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


class ContentHazard(models.Model):
    name = models.CharField(max_length=50)


""" STAKEHOLDER MODELS """


class DockSupervisor(models.Model):
    employee = models.OneToOneField('DockEmployee')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


class DockEmployee(models.Model):
    person = models.OneToOneField('Person')
    dock = models.ForeignKey(Dock, related_name='employees', null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


class ShipCaptain(models.Model):
    person = models.OneToOneField('Person')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bank_account_number = models.CharField(max_length=50)
    home_address = models.ForeignKey('Address')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


class Address(models.Model):
    street_name = models.CharField(max_length=50)
    street_number = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

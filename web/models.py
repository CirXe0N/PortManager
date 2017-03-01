import uuid
from django.contrib.auth.models import User
from django.db import models


""" DOCK & SHIP MODELS """


class Dock(models.Model):
    dock_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    docked_ship = models.OneToOneField('Ship', related_name='dock', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        name = self.name if self.name else '--'
        return '%s [%s]' % (self.dock_id, name)


class DockManifest(models.Model):
    dock = models.ForeignKey(Dock, related_name='manifests')
    ship = models.ForeignKey('Ship')
    arrival = models.DateTimeField()
    departure = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.id)


class Ship(models.Model):
    ship_id = models.CharField(unique=True, max_length=50, db_index=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    captain = models.ForeignKey('ShipCaptain', blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        name = self.name if self.name else '--'
        return '%s [%s]' % (self.ship_id, name)


class Container(models.Model):
    container_id = models.IntegerField(unique=True, db_index=True)
    hazards = models.ManyToManyField('CargoHazard')
    ship = models.ForeignKey('Ship', related_name='containers', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.container_id)

    def get_hazards_string(self):
        return ", ".join([hazard.name for hazard in self.hazards.all()])


class CargoHazard(models.Model):
    name = models.CharField(max_length=50, unique=True)
    web_icon = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


""" STAKEHOLDER MODELS """


class DockSupervisor(models.Model):
    employee = models.OneToOneField('DockEmployee')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return '%s %s' % (self.employee.person.get_first_name(), self.employee.person.get_last_name())


class DockEmployee(models.Model):
    person = models.OneToOneField('Person')
    dock = models.ForeignKey(Dock, related_name='employees', null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return '%s %s' % (self.person.get_first_name(), self.person.get_last_name())

    def is_supervisor(self):
        return bool(self.docksupervisor)
    is_supervisor.boolean = True


class ShipCaptain(models.Model):
    person = models.OneToOneField('Person')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return '%s %s ' % (self.person.get_first_name(), self.person.get_last_name())


class Person(models.Model):
    user = models.OneToOneField(User)
    bank_account_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return '%s %s' % (self.get_first_name(), self.get_last_name())

    def get_first_name(self):
        return self.user.first_name

    def get_last_name(self):
        return self.user.last_name

    def get_email(self):
        return self.user.email


class Address(models.Model):
    ADDRESS_TYPE_CHOICES = (
        ('Home Address', 'Home Address'),
        ('Postal Address', 'Postal Address'),
        ('Other', 'Other'),
    )

    person = models.ForeignKey('Person', null=True)
    address_type = models.CharField(max_length=50, default='Home Address', choices=ADDRESS_TYPE_CHOICES)
    street_name = models.CharField(max_length=50)
    street_number = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    class Meta:
        unique_together = ('person', 'address_type',)

from django.contrib import admin
from .models import Dock, Ship, ShipCaptain, Person, Address, DockEmployee, DockSupervisor, Container, DockManifest, \
    CargoHazard

""" DOCK & SHIP ADMIN VIEWS """


@admin.register(Dock)
class DockAdmin(admin.ModelAdmin):
    list_display = ('dock_id', 'name', 'docked_ship',)


@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    list_display = ('ship_id', 'name', 'captain',)


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ('container_id', 'ship', '_hazards',)

    def _hazards(self, obj):
        return obj.get_hazards_string()
    _hazards.short_description = 'Hazards'


@admin.register(DockManifest)
class DockManifestAdmin(admin.ModelAdmin):
    list_display = ('dock', 'ship', 'arrival', 'departure',)


@admin.register(CargoHazard)
class CargoHazardAdmin(admin.ModelAdmin):
    list_display = ('name',)


""" STAKEHOLDER ADMIN VIEWS """


class HomeAddressInline(admin.StackedInline):
    model = Address
    extra = 1
    max_num = 3


@admin.register(ShipCaptain)
class ShipCaptainAdmin(admin.ModelAdmin):
    list_display = ('person',)


@admin.register(DockEmployee)
class DockEmployeeAdmin(admin.ModelAdmin):
    list_display = ('person', 'is_supervisor',)


@admin.register(DockSupervisor)
class DockSupervisorAdmin(admin.ModelAdmin):
    list_display = ('employee', 'get_email')

    def get_email(self, obj):
        return obj.employee.person.get_email()
    get_email.short_description = 'E-mail'
    get_email.admin_order_field = 'dock_employee__person__email'


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('_last_name', '_first_name', 'user')
    inlines = [HomeAddressInline]

    def _last_name(self, obj):
        return obj.user.last_name
    _last_name.short_description = 'Last Name'
    _last_name.admin_order_field = 'user__last_name'

    def _first_name(self, obj):
        return obj.user.first_name
    _first_name.short_description = 'First Name'
    _first_name.admin_order_field = 'user__first_name'


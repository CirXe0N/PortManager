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
    list_display = ('container_id', 'ship', '_display_hazards',)

    def _display_hazards(self, obj):
        return obj.get_hazards_string()
    _display_hazards.short_description = 'Hazards'


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
    list_display = ('employee',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',)
    inlines = [HomeAddressInline]






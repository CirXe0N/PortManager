import elizabeth
from random import randint
from datetime import timedelta
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.utils.timezone import now
from rest_framework.authtoken.models import Token
from web.models import Person, Address, DockSupervisor, DockEmployee, ShipCaptain, CargoHazard, Ship, Container, Dock, \
    DockManifest


class Command(BaseCommand):
    help = 'Load dummy data for testing and development purpose'

    def handle(self, *args, **options):
        self.load_dummy_data()

    def load_dummy_data(self):
        # Create Container Hazards
        fire_hazard, created = CargoHazard.objects.get_or_create(name='Fire Hazard', web_icon='fa-fire')
        chemical_hazard, created = CargoHazard.objects.get_or_create(name='Chemical Hazard', web_icon='fa-flask')

        used_container_ids = []

        for n in range(0, 50):
            # Create and save dummy person
            dummy = elizabeth.Personal('nl')
            first_name = dummy.name()
            last_name = dummy.surname()
            email = dummy.email()
            bank_account_number = dummy.credit_card_number()

            user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name,
                                            email=email, password='test')

            Token.objects.create(user=user)

            person = Person(user=user, bank_account_number=bank_account_number)
            person.save()

            # Create and save dummy address
            dummy = elizabeth.Address('nl')
            street_name = dummy.street_name()
            street_number = dummy.street_number()
            postal_code = dummy.postal_code()
            city = dummy.city()
            state = dummy.state()
            country = 'The Netherlands'

            Address(person=person, street_name=street_name,
                    street_number=street_number, postal_code=postal_code,
                    city=city, state=state, country=country).save()

            # Create a dummy ship captain, dock employee randomly
            random = randint(1, 10)
            if 4 <= random <= 10:
                DockEmployee(person=person).save()
            else:
                ShipCaptain(person=person).save()

        for n in range(0, 20):
            # Create and save dummy ships
            dummy = elizabeth.Code('nl')
            ship_id = dummy.custom_code(mask='@@@###@@##@@@', char='@', digit='#')

            dummy = elizabeth.Personal()
            name = dummy.name()

            captain = ShipCaptain.objects.filter(ship__isnull=True).first()
            if captain:
                ship = Ship(ship_id=ship_id, name=name, captain=captain)
            else:
                ship = Ship(ship_id=ship_id, name=name)
            ship.save()

            # Create a random amount of containers
            loop_count = 0
            while loop_count < randint(0, 10):

                container_id = randint(1, 100000)
                while container_id in used_container_ids:
                    container_id = randint(1, 100000)
                used_container_ids.append(container_id)

                container = Container(container_id=container_id, ship=ship)
                container.save()

                random = randint(1, 12)
                if random > 9:
                    container.hazards.add(fire_hazard)
                elif 6 <= random <= 9:
                    container.hazards.add(chemical_hazard)
                elif 3 <= random < 6:
                    container.hazards.add(chemical_hazard)
                    container.hazards.add(fire_hazard)
                else:
                    continue
            loop_count += 1

            # Create and save dock randomly
            characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
            random = randint(1, 10)
            if random <= 5:
                name = characters[n].upper()
                dock = Dock(name=name, docked_ship=ship)
                dock.save()

                # Create dock manifests
                DockManifest(dock=dock, ship=ship, arrival=now()).save()

                loop_count = 0
                while loop_count < randint(2, 7):
                    employee = DockEmployee.objects.filter(dock__isnull=True).first()
                    if employee:
                        employee.dock = dock
                        employee.save()
                    loop_count += 1

                employee = DockEmployee.objects.filter(dock=dock).first()
                if employee:
                    DockSupervisor(employee=employee).save()

        # Create Historic dock manifests
        used_ships = []
        ships = Ship.objects.filter(dock__isnull=True)
        docks = Dock.objects.all()
        for index, ship in enumerate(ships):
            if ship not in used_ships:
                random = randint(0, len(docks) - 1)
                dock = docks[random]
                arrival = now() - timedelta(days=index)
                departure = arrival - timedelta(hours=23)
                DockManifest(dock=dock, ship=ship, arrival=arrival, departure=departure).save()

import logging
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import IntegrityError


class Command(BaseCommand):
    help = 'Create a default super user (username: admin, password: test)'

    def handle(self, *args, **options):
        logger = logging.getLogger(__name__)

        try:
            User.objects.create_superuser(username='admin', password='test', email='test@test.abcd')
        except IntegrityError as error:
            logger.warning("DB Error Thrown %s" % error)

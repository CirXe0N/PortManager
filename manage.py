#!/usr/bin/env python
import os
import sys
import pymysql
from PortManager.utilities.env_reader import get_env

if __name__ == "__main__":
    environment = get_env('ENVIRONMENT')

    if environment == 'LOCAL':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PortManager.settings.local')

    if environment == 'TESTING':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PortManager.settings.testing')

    if environment == 'PRODUCTION':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PortManager.settings.production')

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    pymysql.install_as_MySQLdb()
    execute_from_command_line(sys.argv)

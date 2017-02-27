"""
WSGI config for PortManager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from PortManager.utilities.env_reader import get_env

environment = get_env('ENVIRONMENT')

if environment == 'LOCAL':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PortManager.settings.local')

if environment == 'TESTING':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PortManager.settings.testing')

if environment == 'PRODUCTION':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PortManager.settings.production')


application = get_wsgi_application()

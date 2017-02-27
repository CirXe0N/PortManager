import os
import yaml
from django.core.exceptions import ImproperlyConfigured


def get_env(key):
    value = os.environ.get(key, None)
    try:
        if value is None:
            with open('parameters.yml') as f:
                variables = yaml.load(f.read())
            value = variables[key]
        return value
    except(FileNotFoundError, KeyError, TypeError):
        raise ImproperlyConfigured("ImproperlyConfigured: Set %s environment variable." % key)

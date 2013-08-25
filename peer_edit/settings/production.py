"""
Production and global settings.
"""

import os

from . import base
import dj_database_url

DATABASES = {'default': dj_database_url.parse(base.get_env_setting('DATABASE_URL'))}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

STATIC_URL = "/static/"

# SECURITY WARNING: don't run with debug turned on in production!
# Debugging displays nice error messages, but leaks memory. Set this to False
# on all server instances and True only for development.
DEBUG = TEMPLATE_DEBUG = False

# Is this a development instance? Set this to True on development/master
# instances and False on stage/prod.
DEV = False
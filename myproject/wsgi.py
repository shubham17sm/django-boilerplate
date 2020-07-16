"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
from decouple import config

DEBUG = config('DEBUG', cast=bool)

from django.core.wsgi import get_wsgi_application

if DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings.development')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings.production')

application = get_wsgi_application()

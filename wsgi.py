# Copyright 2022 ITCase (info@itcase.pro)

# WSGI config for project.
# It exposes the WSGI callable as a module-level variable named 'application'.
# https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()

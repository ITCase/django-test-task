# Copyright 2022 ITCase (info@itcase.pro)

# ASGI config for project.
# It exposes the ASGI callable as a module-level variable named 'application'.
# https://docs.djangoproject.com/en/dev/howto/deployment/asgi/

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_asgi_application()

"""
ASGI config for helloDjango project.

It exposes the ASGI callable as a game variable.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

____django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '1.settings')

application = get_asgi_application()

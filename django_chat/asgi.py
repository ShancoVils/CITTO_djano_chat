"""
ASGI config for django_chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
import os
import django
from channels.routing import get_default_application
import channels

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_chat.settings')

django.setup()
application = get_default_application()
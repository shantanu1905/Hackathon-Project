"""
ASGI config for configurations project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter , URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from api_floodmanagement.consumers import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configurations.settings')

django_asgi_app = get_asgi_application()


ws_patterns = [
path('ws/notification/' , TestConsumer.as_asgi())


]
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': URLRouter(ws_patterns)
    # Just HTTP for now. (We can add other protocols later.)
})




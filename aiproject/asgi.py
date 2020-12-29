import os

import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter

from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter

import ai_solutions.routing


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aiproject.settings")

django.setup()

application = ProtocolTypeRouter({
  "http": AsgiHandler(),
  "websocket": AllowedHostsOriginValidator( 
    AuthMiddlewareStack(
        URLRouter(
            ai_solutions.routing.websocket_urlpatterns
        )
    ),
  )
})
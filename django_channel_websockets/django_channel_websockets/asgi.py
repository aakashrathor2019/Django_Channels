from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from myapp.routing import websocket_urlpatterns
import os
from django.core.asgi import get_asgi_application
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_channel_websockets.settings')
django.setup()
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                
                websocket_urlpatterns
            )
        )
    }
)
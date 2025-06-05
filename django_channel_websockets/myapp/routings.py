from django.urls import path
from .consumers import ChatConsumer 

websocket_urlpatterns = [
    path('ws/myapp/', ChatConsumer.as_asgi()),
]
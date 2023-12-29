# from channels.routing import ProtocolTypeRouter
# import os
# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nayanRestApi.settings')

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
# })
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from hazardDetect.Consumer import HazardStream
from django.urls import path
from gpsTracking.consumer import MyGpsTracker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nayanRestApi.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(URLRouter([
            path('ws/gpstrack', MyGpsTracker.as_asgi()),
            path('ws/hazardstream', HazardStream.as_asgi())
        ]))
})

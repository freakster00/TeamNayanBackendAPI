# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from django.urls import path

# from gpsTracking.consumer import MyConsumer

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nayanRestApi.settings')

# urlpatterns = [
#     path('ws/gpstrack/', MyConsumer.as_asgi()),
    
# ]

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             urlpatterns
#         )
#     ),
# })
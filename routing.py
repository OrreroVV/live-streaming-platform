# routing.py
from django.urls import re_path, path

from streamingPlatform.consumers.chatSocket.index import ChatSocket

websocket_urlpatterns = [
    # path(r'ws/chat/<str::room_name>/', ChatSocket.as_asgi(), name="chatConsumer"),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatSocket.as_asgi()),
    # path('ws/chat/', ChatSocket.as_asgi(), name="ChatConsumer"),
    #re_path(r'ws/chat/$', ChatSocket.as_asgi()),
    # re_path(r"ws/chat/(?P<root_name>\w+)/$", ChatSocket.as_asgi()),
]

# routing.py
from django.urls import re_path, path

from streamingPlatform.consumers.chatSocket.index import ChatSocket

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatSocket.as_asgi()),
]

# routing.py
from django.urls import re_path, path

from streamingPlatform.consumers.chatSocket.index import ChatSocket
from streamingPlatform.consumers.messageSocket.index import MessageSocket

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatSocket.as_asgi()),
re_path(r'ws/message/(?P<room_name>\w+)/$', MessageSocket.as_asgi()),
]
